var guest = document.getElementById('guestt')
var date = document.getElementById('mdate')

function sendData() {
    fetch('/guest', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data: guest })
    })
    fetch('/date', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data: date })
    })
}