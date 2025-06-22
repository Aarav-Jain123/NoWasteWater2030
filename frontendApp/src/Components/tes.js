const req = fetch("http://127.0.0.1:8000/api/quiz/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    //   "X-CSRFToken": getCSRFToken()
    },
    // credentials: "include",
    body: JSON.stringify({ key: 0 })
  }).then(res => res.json())
    .then(data => {
        console.log(data[0].response[0].choices)
        // console.log(data[0].response[0].question)
    })


console.log(req)

