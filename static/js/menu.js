document.addEventListener("DOMContentLoaded", function(){
    let category = JSON.parse('{{ category | tojson }}')
    alert(category);
});
