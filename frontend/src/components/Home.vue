<template>
    <nav class="navbar">
        <!--img :src="logoPath" alt="CineTick" class="img-logo"-->
        <h3 class="modern">CineTick</h3>
        <div class="search-bar">
            <input type="text" placeholder="Search">
            <a href="#"><i class='bx bx-search-alt'></i></a>
        </div>
        <div class="icons">
            <button type="button" @click="OpenCloseFun()" class="btn btn-danger signup-btn">Signup</button>
            <button type="button" @click="Openlogin()" class="btn btn-danger login-btn">Login</button>
        </div>
    </nav>

    <!--Sign Up-->
    <div v-if="OpenClose" class="modal fade show custom-modal" @click.self="closeModal" tabindex="-1" role="dialog"
        aria-labelledby="exampleModalLabel" aria-hidden="true" style="display: block;">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-body">
                    <div class="signup-container">
                        <div class="signup">
                            <h3 style="color: black;">Sign Up</h3>
                            <input type="text" v-model="name" placeholder="Enter Name" />
                            <input type="text" v-model="email" placeholder="Enter Email" />
                            <input type="password" v-model="password" placeholder="Enter Password" />
                            <button v-on:click="signUp">Create an Account</button>

                        </div>
                    </div>
                    <div class="modal-footer">
                        <!--button type="button" class="btn btn-primary">Save changes</button-->
                        <button type="button" @click="OpenCloseFun()" class="btn btn-primary">Close</button>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <!--Login-->
    <div v-if="openloginModal" class="modal fade show custom-modal" @click.self="Closelogin" tabindex="-1" role="dialog"
        aria-labelledby="exampleModalLabel" aria-hidden="true" style="display: block;">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-body">
                    <div class="signup-container">
                        <div class="signup">
                            <h3 style="color: black;">Login</h3>
                            <input type="text" v-model="email" placeholder="Enter Email" />
                            <input type="password" v-model="password" placeholder="Enter Password" />
                            <button v-on:click="Login">Login</button>
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <!--button type="button" class="btn btn-primary">Save changes</button-->
                    <button type="button" @click="Closelogin()" class="btn btn-primary">Close</button>
                </div>
            </div>
        </div>
    </div>

    <iframe width="1600" height="1200" src="https://lookerstudio.google.com/embed/reporting/91bdf505-5ace-4cc1-b2bd-69f43ff5e089/page/txrhD" frameborder="0" style="border:0" allowfullscreen></iframe>
    <div>
        <div class="container">
            <h1 class="custom-h1">All Movies</h1>
            <div v-for="(movies, city) in categorizedMovies" :key="city">
                <section :id="city" class="category-section">
                    <h3 class="custom-h3">{{ city }}</h3>
                    <div class="movie-row">
                        <div v-for="movie in movies" :key="movie.id" class="card">
                            <div class="card__info">
                                <h6>{{ movie.mname }}</h6>
                                <p>{{ movie.theatre_name }}</p>
                                <p>Date: {{ movie.date }}</p>
                                <p>Time: {{ movie.start_time }} - {{ movie.end_time }}</p>
                                <p>Price: ₹{{ movie.ticket_price }}</p>
                                <p>{{ movie.language }}</p>
                                <p>{{ movie.tags }}</p>
                                <div class="ticket-counter">
                                    <label for="ticket-quantity">Tickets:</label><br>
                                    <input class="ticket-input" type="number" id="ticket-quantity"
                                        v-model="movie.ticketsToBook" min="0" :max="movie.Capacity - movie.ticketsBooked" />
                                </div><br>
                                <button class="btn btn-primary" @click="dummybook()">Book Ticket</button>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'HomePage',
    props: {
        visible: Boolean,

    },
    data() {
        return {
            OpenClose: this.visible,
            openloginModal: false,
            name: '',
            email: '',
            password: '',
            id: '',
            mname: '',
            theatre_name: '',
            city: '',
            date: '',
            start_time: '',
            end_time: '',
            ticket_price: '',
            language: '',
            tags: '',
            addEventModalVisible: false,
            reportModalVisible: false,
            movieList: [],
            categorizedMovies: {},
        }
    },
    methods: {
        closeModal() {
            this.OpenClose = false;
            this.openloginModal = false;
        },

        OpenCloseFun() {
            this.OpenClose = !this.OpenClose;
        },

        Closelogin() {
            this.openloginModal = false;
        },

        Openlogin() {
            this.openloginModal = true;
        },

        async signUp() {

            let result = await axios.post("http://127.0.0.1:5000/auth/signup", {
                name: this.name,
                email: this.email,
                password: this.password
            });

            if (result.status === 200) {
                alert("Signup Successful")
                window.location.reload()
            }

        },
        async Login() {

            let result = await axios.post("http://127.0.0.1:5000/auth/login", {
                email: this.email,
                password: this.password
            });

            console.log("RESULT",result)

            if (result.status === 200) {
                if (result.data.admin) {
                    alert("Admin Login Successful")
                    this.$router.push('/adminhome');
                    localStorage.setItem('adminEmail', this.email);
                    localStorage.setItem('adminToken', result.data.token);
                    localStorage.setItem('isAdmin', true);
                }
                else {
                    const user_id = result.data.user_id; // Extract user_id from the response
                    localStorage.setItem('userEmail', this.email);
                    localStorage.setItem('userToken', result.data.token);
                    localStorage.setItem('isUser', true);
                    localStorage.setItem('user_id', user_id);
                    alert("User Login Successful")
                    this.$router.push('/bookshow');
                }
            }
            else {
                alert("Invalid Credentials")
            }

        },

        


        groupMoviesByCity() {
            this.categorizedMovies = {};
            for (const movie of this.movieList) {
                const city = movie.city;
                if (!this.categorizedMovies[city]) {
                    this.categorizedMovies[city] = [];
                }
                this.categorizedMovies[city].push(movie);
            }
        },

        fetchMoviesData() {
            axios.get('http://127.0.0.1:5000/auth/insert/movies')
                .then(response => {
                    const movies = response.data;
                    this.movieList = movies;
                    this.groupMoviesByCity();

                })
                .catch(error => {
                    console.error('Error fetching movie data:', error);
                });
        },

        dummybook(){
           const confirm = window.confirm("Please Login to book"); 
           if (confirm){
                // Do Nothing
           }
        }
    },

    watch: {
        visible: function (newV, oldV) {
            this.OpenClose = newV;
            this.openloginModal = newV;
            console.log('new' + newV + '==' + oldV)
        }
    },
    mounted() {

        this.fetchMoviesData();


    }

}

</script>

<style>
body,
html {
    margin: 0;
    padding: 0;
    /*background: rgb(255, 255, 255) ; background-image: linear-gradient(to left top, #26045c, #4f0056, #6b004e, #810044, #910839);*/
    background-image: linear-gradient(to left top, #360682, #6e0078, #93006a, #ad005a, #c00a4b);
    background-repeat: no-repeat;
    height: 100%;
}

.modern{
    font-style:italic;
    font-weight: 800;
    text-shadow: 2px 2px 12px rgba(255, 255, 255, 2);
}

.navbar {
    display: flex !important;
    margin: 12px;
    padding: 14px !important;
    background-color: transparent;
    border: 3px solid rgba(118, 118, 118, 0.35);
    border-radius: 12px;
    backdrop-filter: blur(120px);
    color: white;
    box-shadow: 0px 00px 30px rgba(255, 255, 255, 0.45);
}



.icons {
    position: absolute;
    right: 12px;
    margin: 5px;
}

.login-btn {
    margin-left: 12px;
}


.search-bar {
    position: absolute;
    right: 50px;
    left: 50px;
}

.custom-modal {
    background-color: transparent;
    backdrop-filter: blur(1.5px);
}

.ticket-input {
    width: 42%;
    height: 24px;
    padding: 13px;
    border: 1px solid #ccc;
    border-radius: 12px;
    font-size: 16px;
    color: #333;
}
</style>
