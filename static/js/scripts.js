document.addEventListener('DOMContentLoaded', function () {
    fetch('/data')
        .then(response => response.json())
        .then(data => displayItems(data))
        .catch(error => console.error('Error fetching data:', error));
});

function displayItems(data) {
    const container = document.getElementById('items-container');
    container.innerHTML = '';
    for (let page in data) {
        data[page].items.forEach(item => {
            const itemDiv = document.createElement('div');
            itemDiv.className = 'item';
            itemDiv.innerHTML = `
                <h2>${item.Name}</h2>
                <p><strong>Date:</strong> ${item.Date}</p>
                <p><strong>Special Interest Group:</strong> ${item["Special Interest Group"]}</p>
                <p><strong>Originator:</strong> ${item.Originator}</p>
                <p><strong>Gate:</strong> ${item.Gate}</p>
                <p><strong>Owner:</strong> ${item.Owner}</p>
                <p><strong>Areas:</strong> ${item.Areas}</p>
                <p><strong>Idea Pass:</strong> ${item["Idea Pass"]}</p>
                <p><strong>One Pager:</strong> ${item["One Pager"]}</p>
                <p><strong>Score:</strong> ${item.Score}</p>
                <p><strong>Time to Market:</strong> ${item["Time to Market"]}</p>
                <p><strong>Impact:</strong> ${item.Impact}</p>
                <p><strong>Attachment:</strong> ${item.Attachment}</p>
                <p><strong>Source:</strong> ${item.Source}</p>
                <p><strong>Description:</strong> ${item.Description}</p>
                <p><strong>Modified:</strong> ${item.Modified}</p>
                <p><strong>Created:</strong> ${item.Created}</p>
                <p><strong>Legacy ID:</strong> ${item["Legacy ID"]}</p>
                <p><strong>Thumbnail:</strong> <img src="${item.Thumbnail}" alt="Thumbnail"></p>
                <p><strong>To be Revised:</strong> ${item["To be Revised"]}</p>
            `;
            container.appendChild(itemDiv);
        });
    }
}
