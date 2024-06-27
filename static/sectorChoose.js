var info = document.getElementById('info')
var actual = ''

var vip = document.getElementById('vip')
const vipText =  "Ez a legfelső kategóriájú prémium jegyünk.\
A VIP jeggyel rendelkezők prémium székeken ülve, tökéletes látószögből kísérhetik végig a meccs eseményeit.\
Nagy elönye még, hogy a VIP szektorban külön prémium mosdó is található,\
valamint ezen szektorhoz esik a legközelebb a büfé is, ahol nem mellesleg 5% kedvezmény jár VIP jeggyel rendelkező vendégeinknek.\
A VIP jegy előnye még, hogy közvetlenül a VIP szektornál vonulnak be a játékosok,\
így az ilyenfajta jeggyek rendelkezők testközelből láthatják kevdenceiket."



var a = document.getElementById('a')
const aText = "Az A kategóriás helyek a pályához közel helyezkednek el.\
Javasoljuk az olyan nézöinknek, akik igazán nagy rajongók, és az akciódús meccseinket egy pályához közel eső helyröl szeretnék nézni.\
Ha egy igazán nagy rajongó vagy, neked is tökéletes választás lehet,\
hisz a helyek közelsége miatt a játékosok garantáltan hallják a drukkoló szavaidat!\
További előny a hely közelsége miatt, hogy a gyengébben látó nézők is tökéletesen követni tudják az eseményeket."



var b = document.getElementById('b')
const bText = "Ha szereted a magaslatokat, a jó kilátást, és tudsz teli torokból üvölteni a kedvenc csapatodnak,\
vagy csak egyszerűen szereted kielemezni az eseményeket, akkor a B kategóriát neked találtuk ki.\
Ezek a a legjobb ár-érték arányú helyeink. A magasságnak köszönhetően az egész pálya jól belátható,\
nem fogsz egy fontos pillanatról sem lemaradni az garantált!"



var c = document.getElementById('c')
const cText = "A C kategória egy kissé zártabb helyen található. Olyan nézőinknek ajánljuk leginkább, akik szeretnék megnézni a meccset,\
de nem bírják a nagy tömeget, vagy csak nem szeretnének túl sok ember közé keveredni.\
Általában idősebb vendégeink, vagy gyermekes szülők szokták ezeket a helyeket választani.\
Ezen igényeket figyelembe véve, itt található a közelben pelenkázó, valamint az elsösegély-nyújtó is csak egy köpésre van.\
A nézőteret elhagyva pedig hátul egy kisebb játszóteret is kialakítottunk!"



var d = document.getElementById('d')
const dText = "A D kategóriás jegyünk a legolcsóbb jegy. Javasoljuk olyanoknak,\
akik egy felejthetetlen élményben szeretnének részesülni, de nem tudnak, vagy nem akarnak több tízezreket költeni.\
A D kategóriás helyeink a stadion sarkánál lettek kialakítva, de még innen is fenomenális élményben részesül, aki eljön.\
Mi sem bizonyítja a fent említett tényt jobban,\
minthogy az esetek nagy százalékában az összes D kategóriás jegyünk el szokott fogyni." 

var guest = document.getElementById('guest')
const guestText ="A G vagyis Guest azaz Vendég szektor kimondottan a vendég csapat szurkoló táborának lett kialakítva.\
Ha ide tartozol, erősen ajánlott ezt a jegytípust választanod. Természetesen elkülönített ez a szektor a hazai szurkolóktól,\
így biztosan a te kedvenc csapatod szurkolóival leszel egy légtérben. Nincs is jobb élmény, mint együtt szurkolni velük a kedvencednek!"

function unhide(){
    var unhideable = document.getElementById('buy')
    unhideable.removeAttribute('hidden')
}

var path = window.location.pathname
var pathElements = path.split('/')
var pathPlus = pathElements[1]


function actualCall(){
    var buyLink = document.getElementById('buyLink')
    if (actual == 'vipBuy'){
        buyLink.setAttribute('action',String(pathPlus) + '/vip_tickets')
    }
    if (actual == 'aBuy'){
        buyLink.setAttribute('action',String(pathPlus) +  '/a_tickets')
    }
    if (actual == 'bBuy'){
        buyLink.setAttribute('action',String(pathPlus) +  '/b_tickets')
    }
    if (actual == 'cBuy'){
        buyLink.setAttribute('action',String(pathPlus) +  '/c_tickets')
    }
    if (actual =='dBuy'){
        buyLink.setAttribute('action',String(pathPlus) +  '/d_tickets')
    }
    if (actual =='guestBuy'){
        buyLink.setAttribute('action',String(pathPlus) + '/guest_tickets')
    }
}

function textChange(){
    vip.onclick = function() {
        info.innerHTML =  vipText
        actual = 'vipBuy'
        unhide()
        actualCall()
    }
    a.onclick = function() {
        info.innerHTML =  aText
        actual = 'aBuy'
        unhide()
        actualCall()
    }
    b.onclick = function() {
        info.innerHTML =  bText
        actual = 'bBuy'
        unhide()
        actualCall()
    }
    c.onclick = function() {
        info.innerHTML =  cText
        actual = 'cBuy'
        unhide()
        actualCall()
    }
    d.onclick = function() {
        info.innerHTML =  dText
        actual = 'dBuy'
        unhide()
        actualCall()
    }
    guest.onclick = function(){
        info.innerHTML = guestText
        actual = 'guestBuy' 
        unhide()
        actualCall()
    }
}
textChange()

localStorage.clear()


 