var buy1 = document.getElementById('match1')
var buy2 = document.getElementById('match2')
var buy3 = document.getElementById('match3')
var buy4 = document.getElementById('match4')
var buy5 = document.getElementById('match5')
var actual = null


function matchChoose (){
    buy1.onclick = function(){
        var actual = 'meccs1'
        fetch('/actual', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data: actual })
        })
            }
    buy2.onclick = function(){
        var actual = 'meccs2'
        fetch('/actual', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data: actual })
        })
            }
    buy3.onclick = function(){
        var actual = 'meccs3'
        fetch('/actual', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data: actual })
        })
            }
    buy4.onclick = function(){
        var actual = 'meccs4'
        fetch('/actual', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data: actual })
        })
            }
    buy5.onclick = function(){
        var actual = 'meccs5'
        fetch('/actual', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data: actual })
        })
            }
}
matchChoose()


localStorage.clear()

