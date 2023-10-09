from flask import request, jsonify
from models import User, Admin
from database import db
from flask_restful import Resource
import jwt
from functools import wraps
import datetime
import traceback


class Signup(Resource):
    def get(self):
          return 'Ok Tested'

    def post(self):
        try:
            data= request.json
           
            new_user = User(
                name = data['name'],
                email = data['email'],
                password = data['password'],
                role_id=1
            )

            db.session.add(new_user)
            db.session.commit()
                
            return jsonify({"message": "User Created Successfully"}) 
        
        except Exception as e:
            traceback_info = traceback.format_exc()
            return jsonify({"error": str(e), "traceback": traceback_info})

class Login(Resource):
    def get(self):
        try:
            data = request.json
            print("data",data)
            return "Login"
        except Exception as e:
            traceback_info = traceback.format_exc()
            return jsonify({"error": str(e), "traceback": traceback_info})
    
    def post(self):
        try:
            data = request.json
            user = User.query.filter_by(email=data['email']).first()
            admin = Admin.query.filter_by(email=data['email']).first()
           
            if user and user.password == data['password']:
                
                token = generate_token(user)
               
                return ({"message": "Login Successful","token":token,"admin": False, "user_id":user.id}) , 200
            
            elif admin and admin.password == data['password']:
              
                token = generate_token(admin)
                
                return ({"message": "Admin Login Successful","token":token, "admin": True}) , 200
            
            else:
                return jsonify({"message": "Invalid credentials", "token":token, "admin":False}) , 402

        except Exception as e:
            traceback_info = traceback.format_exc()
            return jsonify({"error": str(e), "traceback": traceback_info})
        

def generate_token(user):
    token_payload = {
        "user_id": user.id,
        "role_id": user.role_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
   
    secret_key = "AppDev2Project"  
    algorithm = "HS256"  
  
    token = jwt.encode(token_payload, secret_key, algorithm)
    
    return token


def authorize(role_id, required_permissions=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            token = request.headers.get('Authorization')
            print("tokkkkkkkkennn:",token)
            if not token:
                return jsonify({"message": "Missing token"})
            
            parts = token.split()
            if len(parts) != 2:
                return jsonify({"message": "Invalid authorization header"})

            token_type, actualtoken = parts[0], parts[1]

            if token_type != 'Bearer':
                return jsonify({"message": "Invalid token type"})
            
            try:
                secret_key = "AppDev2Project"  
                algorithm = "HS256"
               
                decoded_token = jwt.decode(actualtoken,secret_key,algorithms=[algorithm])
               
                print("DDDDEEEEECCODE:",decoded_token)  
            except Exception as e:
                traceback_info = traceback.format_exc()
                return jsonify({"error": str(e), "traceback": traceback_info})
            
            # except jwt.exceptions.DecodeError:
            #     return jsonify({"message": "Invalid token"})
            
            # user_id = decoded_token.get('user_id')
            user_role_id = decoded_token.get('role_id')
            print(user_role_id)

            if user_role_id != role_id:
                return jsonify({"message": "Unauthorized"})

            return func(*args, **kwargs)

        return wrapper

    return decorator




