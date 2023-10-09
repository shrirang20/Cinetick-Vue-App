<template>
    <nav class="navbar">
        <!--img :src='logoPath' alt="CineTick" class="img-logo"-->
        <h3 class="modern">CineTick</h3>
        <div class="search-bar">
            <input type="text" placeholder="Search">
            <a href="#"><i class='bx bx-search-alt'></i></a>
        </div>

        <button class="btn btn-danger" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasScrolling"
            aria-controls="offcanvasScrolling">
            Menu
        </button>

    </nav>

    <!--Offcanvas-->
    <div class="offcanvas offcanvas-end" data-bs-scroll="true" data-bs-backdrop="false" tabindex="-1"
        id="offcanvasScrolling" aria-labelledby="offcanvasScrollingLabel">
        <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvasScrollingLabel">Admin</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>

        <div class="offcanvas-body">
            <p><button class="btn1 btn-danger" type="button" @click="openAddTheatreModal">Add Theatre</button></p>
            <p><button class="btn1 btn-danger" type="button" @click="openAddMovieModal">Add Movie</button></p>
            <p><button class="btn1 btn-danger" type="button" @click="openReportModal">Report</button></p>
            <p><button class="btn1 btn-danger" type="button" @click="generateMonthlyReport">Generate Monthly Report</button>
            </p>
            <p><button type="button" @click="Logout()" class="btn1 btn-danger">Logout</button></p>
        </div>
        <div v-if="MonthlyreportGenerated">
            <p>Monthly Report Generated:</p>
            <a :href="reportFileUrl" target="_blank">{{ reportFileUrl }}</a>
        </div>
    </div>

    <!-- Add Theatre Form -->
    <div v-if="addTheatreModalVisible" class="modal fade show custom-modal" @click.self="closeAddTheatreModal" tabindex="-1"
        role="dialog" aria-labelledby="theatreModalLabel" aria-hidden="true" style="display: block;">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-body">

                    <div class="addEvent-container">
                        <div class="modal-footer">
                            <button type="button" @click="closeAddTheatreModal()"
                                class="btn btn-danger close-btn"><strong>x</strong></button>
                        </div>
                        <div class="addEvent">
                            <h3 style="color: black; font:700;">Add Theatre</h3><br>
                            <div class="name">
                                <h6>Theatre Name</h6>
                                <input type="text" v-model="theatrename" placeholder="Enter Theatre name" />
                            </div><br>
                        </div>

                        <div class="name">
                            <h6>City</h6>
                            <input type="text" v-model="theatreCity" placeholder="Enter the theatre City" />
                        </div><br>

                        <div class="Capacity">
                            <h6>Enter Capacity</h6>
                            <input type="text" v-model="Capacity" placeholder="Enter the Capacity" />
                        </div><br>

                        <button class="btn btn-primary" v-on:click="theatressubmit">Submit</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Add Movie Form -->
    <div v-if="addMovieModalVisible" class="modal fade show custom-modal" @click.self="closeAddMovieModal" tabindex="-1"
        role="dialog" aria-labelledby="movieModalLabel" aria-hidden="true" style="display: block;">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-body">

                    <div class="addEvent-container">
                        <div class="modal-footer">
                            <button type="button" @click="closeAddTMovieModal()"
                                class="btn btn-danger close-btn"><strong>x</strong></button>
                        </div>
                        <div class="addEvent">
                            <h3 style="color: black; font:700;">Add Movie</h3><br>
                            <div class="name">
                                <h6>Movie Name</h6>
                                <input type="text" v-model="moviename" placeholder="Enter Movie name" />
                            </div><br>

                            <div class="name">
                                <h6>Theatre Name</h6>
                                <!-- <input type="text" v-model="theatrename" placeholder="Enter Theatre name" > -->
                                <select v-model="theatrename">
                                    <option value="" disabled>Select Theatre name</option>
                                    <option v-for="theatre in theatreNames" :key="theatre">{{ theatre }}</option>
                                </select>
                            </div><br>

                            <div class="name">
                                <h6>City</h6>
                                <!-- <input type="text" v-model="city" placeholder="Select the location" > -->
                                <select v-model="city">
                                    <option value="" disabled>Select the location</option>
                                    <option v-for="cityName in cities" :key="cityName">{{ cityName }}</option>
                                </select>
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
                                <input type="radio" v-model="Language" value="English" id="english"
                                    @onclick="handleradioClick(this)" />
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
                                <input type="radio" v-model="Tags" value="Comedy" id="comedy"
                                    @onclick="handleradioClick(this)" />
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

                            <button class="btn btn-primary" v-on:click="moviessubmit">Submit</button>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!--Report-->
    <div v-if="reportModalVisible" class="modal fade show report-modal" @click.self="closeReportModal" tabindex="-1"
        role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true" style="display: block;">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-body">

                    <div class="report">
                        <div class="modal-footer">
                            <button type="button" @click="closeReportModal()"
                                class="btn btn-danger close-btn"><strong>x</strong></button>
                        </div>
                        <h3 style="color: black; font:700;">Generate Report</h3>
                        <div class="location">
                            Theatre:
                            <select v-model="selectedTheatre" name="theatreId">
                                <option value="" disabled>Select the theatre</option>
                                <option v-for="theatre in theatreList" :key="theatre.id" :value="theatre.id">{{
                                    theatre.tname
                                }}</option>
                            </select>
                        </div><br>
                        <button type="button" @click="generateReport()" class="btn btn-primary">Generate</button>

                        <!-- Display the generated report -->
                        <div v-if="reportGenerated">
                            <h2>Report Generated</h2>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <!--template-->
    <div class="container-cardT">
        <template v-if="categorizedMovies.length > 0">
            <template v-for="(theatreCities, theatreName) in categorizedMovies" :key="theatreName">
                <section :id="theatreName" class="category-section">
                    <h3 class="custom-h3">{{ theatreName }}</h3>
                    <div class="t-buttons">
                        <router-link :to="'/update/' + getTheatreId(theatreName)"
                            class="btn btn-primary custom-t-edit">Edit</router-link>
                        <p><button class="btn btn-danger custom-delete" type="button"
                                @click.self="deletemovie">Delete</button></p>
                    </div>

                    <template v-for="(movies, city) in theatreCities" :key="city">
                        <h4>{{ city }}</h4>
                        <template v-if="movies.length > 0">
                            <div v-for="movie in movies" :key="movie.id" class="card">
                                <div class="card__info">
                                    <h6>{{ movie.mname }}</h6> <!-- Movie Name -->
                                    <p>Date: {{ movie.date }}</p>
                                    <p>Time: {{ movie.start_time }} - {{ movie.end_time }}</p>
                                    <p>Theatre: {{ movie.theatre_name }}</p>
                                    <p>Price: ₹{{ movie.ticket_price }}</p>
                                    <p>Language: {{ movie.language }}</p>
                                    <p>Tags: {{ movie.tags }}</p>

                                </div>
                            </div>
                        </template>
                        <template v-else>
                            <div class="card">
                                <div class="card__info">
                                    <h6>No movies added for this theatre</h6>
                                </div>
                            </div>
                        </template>
                    </template>
                </section>
            </template>
        </template>
        <template v-else>
            <template v-for="(theatreCities, theatreName ) in categorizedMovies" :key="theatreName">
                <section :id="theatreName" class="category-section">
                    <h3 class="custom-h3">{{ theatreName }}
                        <div class="t-buttons">
                            <router-link :to="'/update-theatre/' + theatreName"
                                class="btn btn-primary custom-t-edit">Edit</router-link>
                            <p><button class="btn btn-danger custom-delete" type="button"
                                    @click.self="deleteTheatre(theatreName)">Delete</button></p>
                        </div>
                    </h3>
                    <div class="custom-flex">
                        <template v-for="(movies, city) in theatreCities" :key="city">
                            <div class="custom-h4-card">
                                <h4 class="custom-h4">{{ theatreName }}, {{ city }}</h4>
                                <template v-if="movies.length > 0">
                                    <div v-for="movie in movies" :key="movie.id" class="card">
                                        <div class="card__info">
                                            <h6>{{ movie.mname }}</h6> <!-- Movie Name -->
                                            <p>Date: {{ movie.date }}</p>
                                            <p>Time: {{ movie.start_time }} - {{ movie.end_time }}</p>
                                            <p>Theatre: {{ movie.theatre_name }}</p>
                                            <p>Price: ₹{{ movie.ticket_price }}</p>
                                            <p>Language: {{ movie.language }}</p>
                                            <p>Tags: {{ movie.tags }}</p>
                                            <div class="buttons">
                                                <router-link :to="'/update/' + movie.id"
                                                    class="btn btn-primary custom-edit">Edit</router-link>
                                                <p><button class="btn btn-danger" type="button"
                                                        @click.self="deleteMovie(movie.id)">Delete</button></p>
                                            </div>
                                        </div>
                                    </div>
                                </template>
                                <template v-else>
                                    <div class="card">
                                        <div class="card__info">
                                            <h6>No movies added for this theatre</h6>
                                        </div>
                                    </div>
                                </template>
                            </div>
                        </template>
                    </div>
                </section>
            </template>

        </template>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'AdminHome',

    props: {
        visible: Boolean,
    },

    data() {
        return {
            id: '',
            moviename: '',
            city: '',
            theatrename: '',
            theatreCity: '',
            Capacity: '',
            theatre: '',
            date: '',
            StartTime: '',
            Endtime: '',
            Price: '',
            Language: '',
            Tags: '',
            reportModalVisible: false,
            addTheatreModalVisible: false,
            addMovieModalVisible: false,
            movieList: [],
            theatreList: [],
            categorizedMovies: {},
            selectedTheatre: '',
            theatreNames: [],
            cities: [],
            theatres: [],        // Vue data property to store the list of theatres
            reportGenerated: false,
            reportFileUrl: "",
            MonthlyreportGenerated: false,
            MonthlyreportFileUrl: "",

        }
    },

    methods: {
        closeModal() {
            this.addEventModalVisible = false;
            this.reportModalVisible = false;
        },

        openReportModal() {
            this.reportModalVisible = true;
        },

        closeReportModal() {
            this.reportModalVisible = false;
        },

        openAddTheatreModal() {
            this.addTheatreModalVisible = true;
            this.addMovieModalVisible = false; // Close the movie form if it's open
        },

        closeAddTheatreModal() {
            this.addTheatreModalVisible = false;
        },

        openAddMovieModal() {
            this.addMovieModalVisible = true;
            this.addTheatreModalVisible = false; // Close the theatre form if it's open
        },

        Logout() {
            const adminEmail = localStorage.getItem('adminEmail');
            const adminToken = localStorage.getItem('adminToken');
            const isAdmin = localStorage.getItem('isAdmin');

            if (adminEmail && adminToken && isAdmin) {

                localStorage.removeItem('adminEmail');
                localStorage.removeItem('adminToken');
                localStorage.removeItem('isAdmin');

                this.$router.push('/');
            }
        },

        closeAddTMovieModal() {
            this.addMovieModalVisible = false;
        },

        async generateReport() {
            if (!this.selectedTheatre) { // Use the correct variable name: selectedTheatre
                // Validate that a theater is selected
                return;
            }
            console.log("THIS.SELECTEDTHEATRE:", this.selectedTheatre)
            // Make an HTTP POST request to trigger the CSV export job
            try {
                const response = await axios.post(`http://127.0.0.1:5000/export-theatre-csv/${this.selectedTheatre}`);
                console.log("RESPONSE:", response)


                if (response.status === 200) {
                    // The job has been triggered successfully
                    this.reportGenerated = true;
                    this.reportFileUrl = `/static/reports/theatre_${this.selectedTheatre}_details.csv`;  // Set the URL to the generated report when available

                } else {
                    // Handle errors or display a message if needed
                    console.error("Failed to trigger the export job", response.status);
                }
            } catch (error) {
                console.error("Error while generating the report", error);
            }
        },

        getTheatreId(theatreName) {
            const theatre = this.theatreList.find(t => t.tname === theatreName);
            return theatre ? theatre.id : '';
        },

        handleradioClick(value) {
            const index = this.Language.indexOf(value);
            if (index === -1) {
                this.Language.push(value);
            } else {
                this.Language.splice(index, 1);
            }
        },

        async theatressubmit() {

            let result = await axios.post("http://127.0.0.1:5000/auth/insert", {
                id: this.id,
                tname: this.theatrename,
                city: this.theatreCity,
                capacity: this.Capacity,
            });

            if (result.status === 200) {
                alert("Insert Successful")
                window.location.reload()
            }

        },

        async moviessubmit() {

            let result = await axios.post("http://127.0.0.1:5000/auth/insert/movies", {
                mname: this.moviename,
                theatre_name: this.theatrename,
                city: this.city,
                date: this.date,
                start_time: this.StartTime,
                end_time: this.Endtime,
                ticket_price: this.Price,
                language: this.Language,
                tags: this.Tags,
            });

            if (result.status === 200) {
                alert("Insert Successful")
                window.location.reload()
            }

        },

        async getTheatreCapacity(theatreId) {
            try {
                const response = await axios.get(`http://127.0.0.1:5000/auth/insert/${theatreId}`);
                return response.data.capacity !== undefined ? response.data.capacity : 'N/A';
            } catch (error) {
                console.error('Error fetching theatre capacity:', error);
                return 'N/A'; // Handle errors gracefully
            }
        },

        groupMoviesByTheatre() {
            this.categorizedMovies = {};
            let movieId = 1;
            for (const movie of this.movieList) {
                const theatreName = movie.theatre_name;
                const city = movie.city;
                if (!this.categorizedMovies[theatreName]) {
                    this.categorizedMovies[theatreName] = {};
                }
                if (!this.categorizedMovies[theatreName][city]) {
                    this.categorizedMovies[theatreName][city] = [];
                }
                movie.id = movieId++;
                this.categorizedMovies[theatreName][city].push(movie);
            }
            let theatreId = 1;
            for (const theatre of this.theatreList) {
                const theatreName = theatre.tname;
                const city = theatre.city;

                if (!this.categorizedMovies[theatreName]) {
                    this.categorizedMovies[theatreName] = {};
                }

                if (!this.categorizedMovies[theatreName][city]) {
                    this.categorizedMovies[theatreName][city] = [];
                }

                theatre.id = theatreId++;
            }
        },

        fetchMoviesData() {
            axios.get('http://127.0.0.1:5000/auth/insert/movies')
                .then(response => {
                    const movies = response.data;
                    this.movieList = movies;
                    this.groupMoviesByTheatre();

                })
                .catch(error => {
                    console.error('Error fetching movie data:', error);
                });
        },


        fetchAllTheatresData() {
            axios
                .get('http://127.0.0.1:5000/auth/insert')
                .then((response) => {
                    this.theatreList = response.data;
                })
                .catch((error) => {
                    console.error('Error fetching theatre data:', error);
                });
        },

        deleteMovie(movieID) {
            console.log("movieID", movieID)
            const confirmDelete = window.confirm("Are you sure you want to delete this movie?");
            if (confirmDelete) {
                axios.delete(`http://127.0.0.1:5000/auth/insert/movies/${movieID}`)
                    .then(response => {
                        console.log("response:", response);

                        if (response.status == 200) {
                            console.log("success")
                            alert("Deletion Successful")
                            window.location.reload()
                        } else {
                            console.log("deltion fail:", response.status)
                        }
                    })
                    .catch(error => {
                        console.error("Error deleting movie:", error)
                    })
            }
        },
        deleteTheatre(theatreName) {
            console.log("theatreName:", theatreName)
            const confirmDelete = window.confirm("Are you sure you want to delete this Theatre?");
            if (confirmDelete) {
                axios.delete(`http://127.0.0.1:5000/auth/insert/${theatreName}`)
                    .then(response => {
                        console.log("response:", response);

                        if (response.status == 200) {
                            console.log("success")
                            alert("Deletion Successful")
                            window.location.reload()
                        } else {
                            console.log("deltion fail:", response.status)
                        }
                    })
                    .catch(error => {
                        console.error("Error deleting movie:", error)
                    })
            }
        },

        fetchtheatreNamesAndCities() {
            axios.get('http://127.0.0.1:5000/auth/insert')
                .then(response => {
                    this.theatreList = response.data;

                    this.theatreNames = [...new Set(this.theatreList.map(theatre => theatre.tname))];
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        },



        async pollTaskStatus(taskId) {
            const apiUrl = `http://localhost:5000/check-task-status/${taskId}`;

            try {
                const response = await axios.get(apiUrl);
                console.log("RESPONSE:",response)
                const result = response.data;
                if (result.report_generated) {
                    this.MonthlyreportGenerated = true;
                    this.MonthlyreportFileUrl = result.file_url;
                }

                if (result.email_sent) {
                    alert("Email sent successfully.");
                } else if (result.email_sent === false) {
                    alert("Error: Email sending failed.");
                }

                if (!result.completed) {
                    // Task is not completed yet, continue polling
                    setTimeout(() => {
                        this.pollTaskStatus(taskId);
                    }, 1000); // Poll every 1 second
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred while generating the report.');
            }
        },
        generateMonthlyReport() {
            // Define the API endpoint for generating the report
            const apiUrl = 'http://localhost:5000/generate-monthly-report'; // Replace with your Flask API URL

            // Replace with the recipient's email address
            const recipientEmail = 'official.shriraang@gmail.com';
            axios
                .post(apiUrl, { email: recipientEmail })
                .then((response) => {
                    const result = response.data;
                    if (result.task_id) {
                        // Start polling for task status
                        this.pollTaskStatus(result.task_id);
                    } else {
                        alert(`Error: ${response.data.error}`);
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                    alert('An error occurred while generating the report.');
                });
        },
    },



    created() {
        // Fetch data from your backend and categorize movies by theatreName and city
        this.fetchMoviesData();
        this.fetchAllTheatresData();
        this.fetchtheatreNamesAndCities();
    },
    watch: {
        visible: function (newV, oldV) {
            this.addEventModalVisible = newV;
            this.reportModalVisible = newV;
            console.log('new' + newV + '==' + oldV)
        },
        theatrename: function (newTheatreName) {
            // Update the 'cities' array based on the selected theater name
            this.cities = this.theatreList
                .filter(theater => theater.tname === newTheatreName)
                .map(theater => theater.city);
        },
    },

    mounted() {

        axios.get('http://127.0.0.1:5000/auth/insert')
            .then(response => {
                this.theatreList = response.data;
                console.log(this.theatreList);
                this.groupMoviesByTheatre()
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });

    }
}
</script>

<style>
body,
html {
    margin: 0;
    padding: 5px !important;
    /*background: rgb(255, 255, 255) ; background-image: linear-gradient(to left top, #26045c, #4f0056, #6b004e, #810044, #910839);*/
    background-image: linear-gradient(to left top, #360682, #6e0078, #93006a, #ad005a, #c00a4b);
    background-repeat: no-repeat;
    height: auto !important;
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

.search-bar {
    position: absolute;
    right: 50px;
    left: 50px;
}

.offcanvas-body p {
    padding: 10px;
    text-align: left;
    border: 3px solid rgba(118, 118, 118, 0.35);
    border-radius: 15px;
    box-shadow: 5px 5px 12px rgba(0, 0, 0, 0.2);
    cursor: pointer;
}

.btn1 {
    background-color: transparent !important;
    border: none;
}

.modal-footer {
    border-top: None !important;
}

.close-btn {
    font-size: 14px !important;
    width: 24px;
    height: 24px;
    padding: 0px !important;
    margin: 0px !important;
    border-radius: 7px !important;
}

.marathi,
.hindi,
.tamil,
.action,
.drama,
.romantic,
.Etime,
.etime,
.stime {
    margin-left: 10px;
}

.addEvent-container {
    align-items: center;
    padding: 24px;
    border: 0.5px solid grey;
    border-radius: 12px;
    box-shadow: 0px 0px 24px rgba(0, 0, 0, 0.4);
}

/* Style the Movie Name input field */
.name input[type="text"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    color: #333;
}

/* Style the placeholder text */
.name input[type="text"]::placeholder {
    color: #999;
}

/* Style the input field when focused */
.name input[type="text"]:focus {
    border-color: #007bff;
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

/* Style the select element */
select#venue,
select#loc {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #fffcfc;
    font-size: 16px;
    color: #333;
}

/* Style the selected option */
select#venue option[selected] {
    font-weight: bold;
}

/* Style the placeholder option */
select#venue option[disabled] {
    color: #999;
}

.date input[type="date"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    color: #333;
}

/* Style the time input */

.time input[type="time"] {
    width: 45%;
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

/* Style the time inputs container */
.time {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}


.language,
.tags {
    font-size: 16px;
    color: #333;
}

/* Style the labels for radio buttons */
.language label,
.tags label {
    display: inline-block;
    margin-right: 10px;
    padding: 5px 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    cursor: pointer;
}

/* Style the selected label */
.language input:checked+label,
.tags input:checked+label {
    background-color: #007bff;
    color: white;
    border: 1px solid #007bff;
}

/* Hide the radio inputs */
.language input,
.tags input {
    display: none;
}

/* Style the label when hovered */
.language label:hover,
.tags label:hover {
    background-color: #f2f2f2;
}

/* Style the label when focused (keyboard navigation) */
.language label:focus,
.tags label:focus {
    outline: none;
    box-shadow: 0 0 3px #007bff;
}

.Capacity input[type="text"],
.Tprice input[type="text"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    color: #333;
}

/* Style the placeholder text */
.Capacity input[type="text"]::placeholder,
.Tprice input[type="text"]::placeholder {
    color: #999;
}

/* Style the input fields when focused */
.Capacity input[type="text"]:focus,
.Tprice input[type="text"]:focus {
    border-color: #007bff;
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

.report {
    padding: 15px;
    border: 1.5px solid grey;
    border-radius: 12px;
    box-shadow: 0px 0px 24px rgba(0, 0, 0, 0.4);
}


.card {

    background-color: #fff;
    border: 2px solid grey !important;
    border-radius: 12px !important;
    box-shadow: 0 0px 20px rgba(255, 255, 255, 0.5) !important;
    margin-bottom: 20px;
    padding: 20px;
    width: 200px;
    margin: 5px;
}

/* Style movie details */
.card__info {

    font-size: 16px;
    color: #444;

}

.custom-h1 {
    font-size: 28px;
    color: #fffdfd;
    font-weight: 900;
    text-shadow: grey;
}

.custom-h3 {
    font-size: 24px;
    color: #fff;
    margin-bottom: 10px;
    font-weight: 800;
    border: 2px solid darkgrey;
    border-radius: 12px;
    box-shadow: 0 0 10px rgba(256, 256, 256, 1.6);
    margin: 14px;
}

.custom-h4 {
    font-size: 24px;
    color: #fff;
    margin-bottom: 10px;
    font-weight: 800;
    border: 2px solid darkgrey;
    border-radius: 12px;
    box-shadow: 0 0 10px rgba(256, 256, 256, 1.6);
    width: 200px;
    margin: 5px;
}

/* Style tags */
.card__info p:last-child {
    font-weight: bold;
}

/* Add some spacing between elements */
.movie-row {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

/* Media query for responsive design */
@media (max-width: 768px) {
    .card {
        width: 100%;
    }
}

/*.container-cardT{
   display: flex;
   flex-direction: row;
   margin: 0px !important;
}*/

.custom-flex {
    display: flex;
    flex-direction: row;
    margin: 12px !important;
}

.custom-h4-card {
    display: flex;
    flex-direction: column;
    margin: 0px !important;
}

.buttons {
    display: flex;
    justify-content: space-between;
}

.t-buttons {
    display: flex;
    margin-left: 44%;
}

.custom-t-edit {
    width: 74px;
    height: 38px;
    margin: 5px;
}

.custom-delete {
    margin: 5px
}

.custom-edit {
    width: 74px;
    height: 38px;
}
</style>
