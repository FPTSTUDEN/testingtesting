///logging form response to console
const form = document.querySelector('form');
///https://api.chucknorris.io/jokes/random
async function getjoke(params) {
    random_joke=await fetch('https://api.chucknorris.io/jokes/random');
///fetch -> json
    data = await random_joke.json();
    console.log(data.value)
}
getjoke();
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission behavior
    // const formData = new FormData(form);
    // const queryString = new URLSearchParams(formData).toString();
    // console.log('Form submitted with data:', queryString);
    const api_response = fetch(`https://api.tvmaze.com/search/shows?q=${document.getElementById('query').value}`)
        ///.then(variable => do something with variable)
        .then(response => response.json()) ///parse to json
        .then(data => console.log(data)) ///log data variable (parsed json)
        .catch(error => console.error('Error fetching data:', error));
    let resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = ''; ///clear previous results
    const data=fetch(`https://api.tvmaze.com/search/shows?q=${document.getElementById('query').value}`)
    .then(response => response.json())
    .then(data => {
    console.log(data.value);
    for (let item of data) {
        let show = item.show;
        resultsDiv.innerHTML += `<h2>${show.name}</h2>
        <a href="${show.url}" target="_blank">More Info</a>
        <img src="${show.image ? show.image.medium : 'https://placehold.co/210x295?text=Not%20Found'}" alt="${show.name} Poster"/>
        <div>${show.summary}</div>`;
    }
    });
});