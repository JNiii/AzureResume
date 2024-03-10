window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount();
})

const localfunctionApi = 'http://localhost:7071/api/GetAzureResume';
const azurefunctionApi = 'https://fa-azurewebresume.azurewebsites.net/api/GetAzureResume?';

const getVisitCount = () => {
    let count = 1;
    fetch(azurefunctionApi).then(response => {
        return response.json()
    }).then(response =>{
        console.log("Website called function API.");
        count = response.count;
        document.getElementById("counter").innerText = count;
    }).catch(function(error){
        console.log(error);
    });
    return count;
}