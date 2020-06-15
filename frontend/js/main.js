const search = document.getElementById('search');
const list = document.getElementById('search-list');
var res_json = [];

//

const searchTextServer = async searchText => {
    var formdata = new FormData();
    formdata.append("keyword", searchText);
    const res = await fetch('http://127.0.0.1:8000/search', {
        mode: 'cors',
        method: 'POST',
        body: formdata,
    });
    res_json = await res.json();
    return res_json;
};

const searchTextlocal = async searchText => {
    while (searchText.length <= 3) {
            list.innerHTML = '';
            return null;
    }

    res_json = searchTextServer(searchText).then(res_json =>{

        if (res_json.length >= 500) {
            res_json = res_json.filter(v => v['text'].includes(searchText));
        }
        outputHtml(res_json);
    });
};

//
const outputHtml = results => {
    if (results.length > 0) {
        const html = results.map(result =>
        `
            <div class="card card-body mb-1">
                <h4>
                ${result.text.substring(0, result.text.search(new RegExp(search.value, 'i')))}
                <span class='highlight' style="color: blue;">
                ${result.text.substring(result.text.search(new RegExp(search.value, 'i')),
                 result.text.search(new RegExp(search.value, 'i')) + search.value.length)}
                </span>
                ${result.text.substring(result.text.search(new RegExp(search.value, 'i')) + search.value.length)}
                </h4>
                <small>score: ${result.score} helpfulness: ${result.helpfulness}</small>
            </div>
        `).join('');
        list.innerHTML = html;
    }
};

search.addEventListener('input', () => searchTextlocal(search.value));

