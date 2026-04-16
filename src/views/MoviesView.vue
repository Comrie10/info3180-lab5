<script setup>
    import { ref, onMounted } from "vue";
    let movies = ref([]);

    function fetchMovies(){
        fetch("/api/v1/movies")
            .then(res => res.json())
            .then (data => {
                movies.value = data.movies;
            })
            .catch (error => console.log(error));
    }
    onMounted(() => {
        fetchMovies();
    });
</script>
<template>
    <div class="container mt-4">
        <h1>Movies</h1>
        <div class="row">
            <div v-for="movie in movies" :key="movie.id">
                <div class="card" style="max-width:25%">
                    <img :src="`http://localhost:5001/api/v1/posters/${movie.poster}`" class="card-img" style="max-width:50%; max-height: 100%;" />
                    <div class="body">
                        <h4 class="title">{{movie.title}}</h4>
                        <p class="description">{{movie.description}}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>