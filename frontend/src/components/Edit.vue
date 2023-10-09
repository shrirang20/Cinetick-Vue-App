<template>
    <!--Edit Event-->
    <div class="EditEvent-container">
        <div class="addEvent">
            <h3 style="color: black; font:700;">Edit Movie</h3><br>
            <div class="name">
                <h6>Movie Name</h6>
                <input type="text" v-model="moviename" placeholder="Enter Movie name" />
            </div><br>

            <div class="name">
                <h6>Theatre Name</h6>
                <input type="text" v-model="theatrename" placeholder="Enter Theatre name" />
            </div><br>

            <div class="name">
                <h6>City</h6>
                <input type="text" v-model="city" placeholder="Select the location" />
            </div><br>

            <div class="date">
                <h6>Select Date</h6>
                <input type="date" id="date" v-model="date" name="date">
            </div><br>

            <div class="time">
                <label class="Stime">Start Time:</label>
                <input type="time" id="Stime" v-model="StartTime" name="Stime" class="stime">

                <label class="Etime">End Time:</label>
                <input type="time" id="Etime" v-model="Endtime" name="Etime" class="etime">
            </div><br>

            <div class="Tprice">
                <h6>Ticket Price</h6>
                <input type="text" v-model="Price" placeholder="Enter the Ticket price" />
            </div><br>

            <div class="language">
                <h6>Select the Language </h6> <br>
                <input type="radio" v-model="Language" value="English" id="english" @onclick="handleradioClick(this)" />
                <label for="english">English</label>

                <input type="radio" v-model="Language" value="Hindi" id="hindi" class="hindi"
                    @onclick="handleradioClick(this)" />
                <label for="hindi">Hindi</label>

                <input type="radio" v-model="Language" value="Marathi" id="marathi" class="marathi"
                    @onclick="handleradioClick(this)" />
                <label for="marathi">Marathi</label>

                <input type="radio" v-model="Language" value="Tamil" id="tamil" class="tamil"
                    @onclick="handleradioClick(this)" />
                <label for="tamil">Tamil</label>
            </div><br>


            <div class="tags">
                <h6>Select the Tags</h6> <br>
                <input type="radio" v-model="Tags" value="Comedy" id="comedy" @onclick="handleradioClick(this)" />
                <label for="comedy">Comedy</label>
                <input type="radio" v-model="Tags" value="Action" id="action" class="action"
                    @onclick="handleradioClick(this)" />
                <label for="action">Action</label>
                <input type="radio" v-model="Tags" value="Drama" id="drama" class="drama"
                    @onclick="handleradioClick(this)" />
                <label for="drama">Drama</label>
                <input type="radio" v-model="Tags" value="Romantic" id="romantic" class="romantic"
                    @onclick="handleradioClick(this)" />
                <label for="romantic">Romantic</label>
            </div><br>

            <button class="btn btn-primary" v-on:click="movieeditsubmit(theatreId)">Submit</button>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'EditShows',

    data() {
        return {
            id: '',
            moviename: '',
            theatrename: '',
            city: '',
            date: '',
            StartTime: '',
            Endtime: '',
            Capacity: '',
            Price: '',
            Language: '',
            Tags: '',
            theatreId: null
        }
    },
    methods: {
        handleradioClick(value) {
            const index = this.Language.indexOf(value);
            if (index === -1) {
                this.Language.push(value);
            } else {
                this.Language.splice(index, 1);
            }
        },

        async movieeditsubmit() {
            try {
                const data = {
                    id: this.id,
                    mname: this.moviename,
                    theatre_name: this.theatrename,
                    city: this.city,
                    date: this.date,
                    start_time: this.StartTime,
                    end_time: this.Endtime,
                    ticket_price: this.Price,
                    language: this.Language,
                    tags: this.Tags,
                };

                const response = await axios.put(`http://127.0.0.1:5000/auth/insert/movies/${this.theatreId}`, data);

                if (response.data.message === "Updation Sucessful") {
                    alert("Movie updated successfully!");
                    this.$router.push('/adminhome')
                } else {
                    alert("Movie update failed! Either Theatre or City doesn't exist");
                    this.$router.push('/adminhome')
                }
            } catch (error) {
                console.error('Error updating movie:', error);
            }
        },

       
    },
    async mounted() {
            try {
                let m_id = this.$route.params.id;
                console.log("edit page params.id:", m_id);
                const response = await axios.get(`http://127.0.0.1:5000/auth/insert/movies/${m_id}`);
                console.log("response data", response.data);

                this.moviename = response.data.mname;
                this.city = response.data.city;
                this.theatrename = response.data.theatre_name;
                this.date = response.data.date;
                this.StartTime = response.data.start_time;
                this.Endtime = response.data.end_time;
                this.Capacity = response.data.theatre_id;
                this.Price = response.data.ticket_price;
                this.Language = response.data.language;
                this.Tags = response.data.tags;
                this.theatreId = m_id;
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        },
}
</script>

<style>
.EditEvent-container {
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
}</style>