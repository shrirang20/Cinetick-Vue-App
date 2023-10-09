<template>
    <nav class="navbar">
        <!--img :src="logoPath" alt="CineTick" class="img-logo"-->
        <h3 class="modern">CineTick</h3>

        <!-- <div class="search-bar">
            <input type="text" placeholder="Search">
            <a href="#"><i class='bx bx-search-alt'></i></a>
        </div> -->

        <div class="search-bar">
            <input type="text" placeholder="Search" @input="searchMovies" v-model="searchQuery">
            <div v-if="searchResults.length > 0" class="search-dropdown">
                <ul>
                    <li v-for="result in searchResults" :key="result.id">
                        <!-- <a @click="selectMovie(result)" v-html="highlightSearch(result.mname)"></a><br> -->
                        <a @click="selectMovie(result)" :class="{'highlighted': result.highlighted}">
                            <div class="movie-info">
                                <div class="movie-name">{{ result.mname }}</div> 
                                <span></span>
                                <div class="movie-details">
                                    <div class="details-left">
                                        <p>{{ result.ticket_price }}</p>
                                        <p>{{ result.language }}</p>
                                    </div>
                                    <div class="details-right">
                                        <p>{{ result.theatre_name }}</p>
                                        <p>{{ result.tags }}</p>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </li>
                </ul>
            </div>
        </div>

        <div class="icons">
            <button type="button" @click="Logout()" class="btn btn-danger login-btn">Logout</button>
        </div>
    </nav>

    <!--Movie template-->
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
                                <button class="btn btn-primary" @click="bookTicket(movie)">Book Ticket</button>
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
    name: 'LandingPage',
    data() {
        return {
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
            categorizedMovies: {},
            searchQuery: '',
            searchResults: [],
        }
    },
    methods: {

        Logout() {
            const userEmail = localStorage.getItem('userEmail');
            const userToken = localStorage.getItem('userToken');
            const isUser = localStorage.getItem('isUser');
            const user_id = localStorage.getItem('user_id');


            if (userEmail && userToken && isUser && user_id) {

                localStorage.removeItem('userEmail');
                localStorage.removeItem('userToken');
                localStorage.removeItem('isUser');
                localStorage.removeItem('user_id');

                this.$router.push('/');
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

        async bookTicket(movieId) {
            console.log("MOVIE:", movieId.id)
            const user_id = localStorage.getItem('user_id');
            console.log("USER_ID:", user_id)

            try {
                const response = await axios.post(`http://127.0.0.1:5000/auth/book-ticket/${movieId.id}`, {
                    user_id: user_id,
                    movieId: movieId.id,
                    num_tickets: movieId.ticketsToBook,
                });
                console.log("RESPONSE:", response)
                if (response.status === 200) {
                    alert('Ticket booked successfully');
                    // Perform any additional actions after booking the ticket
                }
            } catch (error) {
                console.error('Error booking ticket:', error);
            }
        },
        searchMovies() {
            // Send an API request to search for movies
            if (this.searchQuery.trim() === '') {
                this.searchResults = []; // Clear the dropdown if the query is empty
            } else {
                // Replace this with your actual API endpoint for searching movies
                const apiUrl = `http://127.0.0.1:5000/auth/search-movies?query=${encodeURIComponent(this.searchQuery)}`;

                axios.get(apiUrl)
                    .then(response => {
                        this.searchResults = response.data.movies;
                    })
                    .catch(error => {
                        console.error('Error searching movies:', error);
                    });
            }
        },


        highlightSearch(movieName) {
            // Create a regular expression to match the search query
            const query = this.searchQuery.trim();
            const regex = new RegExp(`(${query})`, 'gi');

            // Replace the matched query with HTML to highlight it
            return movieName.replace(regex, '<span class="highlighted">$1</span>');
        },
        selectMovie(movie) {
            // Handle when a movie is selected from the dropdown
            // You can perform actions like redirecting to the movie details page here
            console.log('Selected movie:', movie);
        },
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

.modern {
    font-style: italic;
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

.search-dropdown {
    color: black;
    width: 50%;
    position: absolute; /* Position the dropdown absolutely */
    top: 100%; /* Position below the input */
    left:24%; /* Align with the left edge of the input */ 
    z-index: 1; /* Ensure the dropdown is above other content */
    background-color: #fff; /* Background color of the dropdown */
    border: 1px solid #ccc; /* Add a border for styling */
    border-radius: 20px;
    max-height: 450%; /* Limit the max height of the dropdown to avoid excessive scrolling */
    overflow-y: auto; /* Enable vertical scrolling if needed */
    list-style-type: none; /* Remove bullet points */
    padding: 0; /* Remove default padding */
    margin: 0; /* Remove default margin */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  /* Add a shadow for a nice effect */
}

.search-dropdown ul {
    padding: 0;
    /* Remove default padding from the ul inside the dropdown */
    margin: 0;
    /* Remove default margin from the ul inside the dropdown */
}

.search-dropdown li {
    padding: 10px;
    /* Add padding to the list items for spacing */
    border-bottom: 1px solid #eee;
    /* Add a bottom border to separate items */
}

.highlighted {
    background-color: yellow; /* Change to your desired highlight color */
    color:red;
    font-weight: bold; /* Optionally make the text bold */
}

.movie-info {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    flex-direction: column;
}

.movie-name {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 5px;
}

.movie-details {
    display: flex;
    justify-content: space-evenly;
    width: 100%;
}

.details-left, .details-right {
    width: 0%; /* Adjust as needed */
}

.details-left p, .details-right p {
    margin: 0;
    font-size: 14px;
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
}</style>