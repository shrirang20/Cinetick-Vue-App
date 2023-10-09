<template>
    <!--Edit Event-->
    <div class="EditTheatre-container">
        <div class="addEvent">
            <h3 style="color: black; font:700;">Edit Movie</h3><br>
            <div class="name">
                <h6>Theatre Name</h6>
                <input type="text" v-model="theatrename" placeholder="Enter Theatre name" />
            </div><br>
            <button class="btn btn-primary" v-on:click="theatreeditsubmit(theatreId)">Submit</button>

        </div>
    </div>
</template>

<script>
import axios from 'axios'



export default {
    name: 'EditTheatre',

    data() {
        return {
            id: '',
            theatrename: '',
            theatreId: null
        }
    },

    methods: {   

    async theatreeditsubmit() {
      try {
        const data = {
          tname: this.theatrename,
        };
        const response = await axios.put(`http://127.0.0.1:5000/auth/insert/${this.theatreId}`, data);
        console.log(response)
        if (response.data.message === "Successfully Updated Theatre") {
          alert("Theatre updated successfully!");
          this.$router.push('/adminhome')
        } else {
          alert("Theatre update failed! Either Theatre or City doesn't exist");
          this.$router.push('/adminhome')
        }
      } catch (error) {
        console.error('Error updating movie:', error);
      }
    },
    },

    async mounted() {
        try {
            let m_id = this.$route.params.theatrename;
            const response = await axios.get(`http://127.0.0.1:5000/auth/insert/${m_id}`);            
            this.theatrename = response.data.tname;
            this.theatreId = m_id;
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    },
}
</script>

<style>
.EditTheatre-container {
    align-items: center;
    padding: 24px;
    border: 0.5px solid grey;
    border-radius: 12px;
    box-shadow: 0px 0px 24px rgba(0, 0, 0, 0.4);
    background-color: white;
    backdrop-filter: blur(30px);
    width: 38%;
    margin: 20px;
    margin-left: 32%;
    margin-top: 200px;
    margin-bottom: 237.5px;
}



/* Style the Movie Name input field */
.editname input[type="text"] {
    width: 50%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    color: #333;
}

/* Style the placeholder text */
.editname input[type="text"]::placeholder {
    color: #999;
}

/* Style the input field when focused */
.editname input[type="text"]:focus {
    border-color: #007bff;
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

/* Style the select element */
select#editvenue,
select#editloc {
    width: 50%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #fffcfc;
    font-size: 16px;
    color: #333;
}

/* Style the selected option */
select#editvenue option[selected] {
    font-weight: bold;
}

/* Style the placeholder option */
select#editvenue option[disabled] {
    color: #999;
}

.editdate input[type="date"] {
    width: 50%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    color: #333;
}

/* Style the time input */

.edittime input[type="time"] {
    width: 10%;
    /* Adjust the width as needed */
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    color: #333;
}

/* Style the labels for time inputs */
.label {
    font-size: 16px;
    margin-right: 10px;
}


.editlanguage,
.edittags {
    font-size: 16px;
    color: #333;
}

/* Style the labels for radio buttons */
.editlanguage label,
.edittags label {
    display: inline-block;
    margin-right: 10px;
    padding: 5px 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    cursor: pointer;
}

/* Style the selected label */
.editlanguage input:checked+label,
.edittags input:checked+label {
    background-color: #007bff;
    color: white;
    border: 1px solid #007bff;
}

/* Hide the radio inputs */
.editlanguage input,
.edittags input {
    display: none;
}

/* Style the label when hovered */
.editlanguage label:hover,
.edittags label:hover {
    background-color: #f2f2f2;
}

/* Style the label when focused (keyboard navigation) */
.editlanguage label:focus,
.edittags label:focus {
    outline: none;
    box-shadow: 0 0 3px #007bff;
}

.editCapacity input[type="text"],
.editTprice input[type="text"] {
    width: 50%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    color: #333;
}

/* Style the placeholder text */
.editCapacity input[type="text"]::placeholder,
.editTprice input[type="text"]::placeholder {
    color: #999;
}

/* Style the input fields when focused */
.editCapacityinput[type="text"]:focus,
.editTprice input[type="text"]:focus {
    border-color: #007bff;
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}
</style>