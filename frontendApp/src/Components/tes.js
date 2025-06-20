const req = fetch(
    "http://127.0.0.1:8000/api/fact-abt-water/",
    ).then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.log(err));

console.log(req)

