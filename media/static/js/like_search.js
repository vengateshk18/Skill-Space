document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.likeButton').forEach(function (likeButton) {
        likeButton.addEventListener('click', function (e) {
            e.preventDefault();
            //console.log('Clicked like button');

            var post_id = likeButton.getAttribute('data-post-id');
            var likesCountElement = likeButton.querySelector('p');

            if (post_id) {
                fetch('/like_post?id=' + post_id, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}',
                    },
                })
                .then(response => response.json())
                .then(data => {
                    //console.log('Server response:', data);

                    if (data.success) {
                        //console.log('Updating UI...');
                        likesCountElement.textContent = data.likes_count > 0 ?
                            (data.likes_count === 1 ? 'Liked by 1 person' : 'Liked by ' + data.likes_count + ' people') :
                            'No likes';

                        // Toggle the button text based on the response
                        likeButton.querySelector('svg').classList.toggle('liked', data.has_liked);
                    } else {
                        console.error('Server error:', data.error);
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            }
        });
    });
});



$(document).ready(function () {
    // Trigger search on input change
    $('#username').on('input', function () {
        searchUser();
    });
});

function searchUser() {
    var query = $('#username').val();

    $.ajax({
        url: '/username_suggestions/',
        data: {'query': query},
        dataType: 'json',
        success: function(data) {
            displaySuggestions(data.suggestions);
        }
    });
}

function displaySuggestions(suggestions) {
    var suggestionsContainer = $('#suggestions-container');
    suggestionsContainer.empty();

    if (suggestions.length > 0) {
        var list = $('<ul>');
        suggestions.forEach(function(username) {
            list.append('<li>' + username + '</li>');
        });
        suggestionsContainer.append(list);
    } else {
        suggestionsContainer.append('<p>No suggestions found.</p>');
    }
}

import { Autocomplete, Input, Ripple, initMDB } from "mdb-ui-kit";

initMDB({ Input, Ripple });

const basicAutocomplete = document.querySelector('#search-autocomplete');
const data = ['One', 'Two', 'Three', 'Four', 'Five'];
const dataFilter = (value) => {
return data.filter((item) => {
return item.toLowerCase().startsWith(value.toLowerCase());
});
};

new Autocomplete(basicAutocomplete, {
filter: dataFilter
});

///
document.addEventListener("DOMContentLoaded", function () {
    var input = document.getElementById("username");
    var suggestionsContainer = document.getElementById("suggestions-container");

    input.addEventListener("input", function () {
        searchUser();
    });

    function searchUser() {
        var query = input.value.trim();

        if (query === "") {
            suggestionsContainer.style.display = "none";
            return;
        }

        // Perform your AJAX request to get suggestions here
        // For simplicity, let's assume suggestions is an array of strings
        var suggestions = ["User1", "User2", "User3"];

        displaySuggestions(suggestions);
    }

    function displaySuggestions(suggestions) {
        suggestionsContainer.innerHTML = "";

        if (suggestions.length > 0) {
            var list = document.createElement("ul");
            suggestions.forEach(function (username) {
                var listItem = document.createElement("li");
                listItem.textContent = username;
                listItem.addEventListener("click", function () {
                    input.value = username;
                    suggestionsContainer.style.display = "none";
                });
                list.appendChild(listItem);
            });
            suggestionsContainer.appendChild(list);
            suggestionsContainer.style.display = "block";
        } else {
            suggestionsContainer.style.display = "none";
        }
    }

    // Close suggestions when clicking outside the input and suggestions container
    document.addEventListener("click", function (event) {
        if (!event.target.closest(".search-container")) {
            suggestionsContainer.style.display = "none";
        }
    });
});