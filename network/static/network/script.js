document.addEventListener("DOMContentLoaded", function () {
  // Render Brightness
  brightness();

  // User being seen as prifile
  try {
    // Get user profile user id from template
    const user_profile = JSON.parse(
      document.getElementById("user_profile").textContent
    );
    // Run function
    get_user(user_profile);
  } catch (TypeError) {}

  // Save button
  try {
    document
      .querySelectorAll('[data-type="text-area-save"]')
      .forEach((button) => {
        button.addEventListener("click", () => {
          id = button.dataset.id;
          edit_idea(id);
        });
      });
  } catch (TypeError) {}
  // END Edit idea save button

  // Edit button takes off alert
  try {
    document
      .querySelectorAll('[data-type="text-area-edit"]')
      .forEach((button) => {
        button.addEventListener("click", () => {
          id = button.dataset.id;
          document.querySelector(`#alert-${id}`).style.display = "none";
        });
      });
  } catch (TypeError) {}
  // END Edit idea save button

});

// Idea Brighten
function brighten(id) {
  fetch("/", {
    method: "PUT",
    headers: { "X-CSRFToken": csrftoken },
    mode: "same-origin",
    body: JSON.stringify({
      id: id,
      bright: true,
    }),
  }).then((response) => brightness());
}

// Idea Darken
function darken(id) {
  fetch("/", {
    method: "PUT",
    headers: { "X-CSRFToken": csrftoken },
    mode: "same-origin",
    body: JSON.stringify({
      id: id,
      dark: true,
    }),
  }).then((response) => brightness());
}

// Render Buttons
function brightness() {
  fetch("/ideas")
    .then((response) => response.json())
    .then((ideas) => {
      ideas.forEach((idea) => {
        const id = idea.id;
        const lumen = idea.lumen;
        const user_id = JSON.parse(
          document.getElementById("user_id").textContent
        );

        if (idea.bright.includes(user_id)) {
          var btn_bright = `<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="#e6ac00" class="bi bi-lightbulb-fill" viewBox="0 0 16 16">
          <path d="M2 6a6 6 0 1 1 10.174 4.31c-.203.196-.359.4-.453.619l-.762 1.769A.5.5 0 0 1 10.5 13h-5a.5.5 0 0 1-.46-.302l-.761-1.77a1.964 1.964 0 0 0-.453-.618A5.984 5.984 0 0 1 2 6zm3 8.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1l-.224.447a1 1 0 0 1-.894.553H6.618a1 1 0 0 1-.894-.553L5.5 15a.5.5 0 0 1-.5-.5z"/>
        </svg>`;
        } else {
          var btn_bright = `<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" class="bi bi-lightbulb" viewBox="0 0 16 16">
          <path d="M2 6a6 6 0 1 1 10.174 4.31c-.203.196-.359.4-.453.619l-.762 1.769A.5.5 0 0 1 10.5 13a.5.5 0 0 1 0 1 .5.5 0 0 1 0 1l-.224.447a1 1 0 0 1-.894.553H6.618a1 1 0 0 1-.894-.553L5.5 15a.5.5 0 0 1 0-1 .5.5 0 0 1 0-1 .5.5 0 0 1-.46-.302l-.761-1.77a1.964 1.964 0 0 0-.453-.618A5.984 5.984 0 0 1 2 6zm6-5a5 5 0 0 0-3.479 8.592c.263.254.514.564.676.941L5.83 12h4.342l.632-1.467c.162-.377.413-.687.676-.941A5 5 0 0 0 8 1z"/>
        </svg>`;
        }

        if (idea.dark.includes(user_id)) {
          var btn_dark = `<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="black" class="bi bi-lightbulb-off-fill" viewBox="0 0 16 16">
          <path d="M2 6c0-.572.08-1.125.23-1.65l8.558 8.559A.5.5 0 0 1 10.5 13h-5a.5.5 0 0 1-.46-.302l-.761-1.77a1.964 1.964 0 0 0-.453-.618A5.984 5.984 0 0 1 2 6zm10.303 4.181L3.818 1.697a6 6 0 0 1 8.484 8.484zM5 14.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1l-.224.447a1 1 0 0 1-.894.553H6.618a1 1 0 0 1-.894-.553L5.5 15a.5.5 0 0 1-.5-.5zM2.354 1.646a.5.5 0 1 0-.708.708l12 12a.5.5 0 0 0 .708-.708l-12-12z"/>
        </svg>`;
        } else {
          var btn_dark = `<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" class="bi bi-lightbulb-off" viewBox="0 0 16 16">
          <path fill-rule="evenodd" d="M2.23 4.35A6.004 6.004 0 0 0 2 6c0 1.691.7 3.22 1.826 4.31.203.196.359.4.453.619l.762 1.769A.5.5 0 0 0 5.5 13a.5.5 0 0 0 0 1 .5.5 0 0 0 0 1l.224.447a1 1 0 0 0 .894.553h2.764a1 1 0 0 0 .894-.553L10.5 15a.5.5 0 0 0 0-1 .5.5 0 0 0 0-1 .5.5 0 0 0 .288-.091L9.878 12H5.83l-.632-1.467a2.954 2.954 0 0 0-.676-.941 4.984 4.984 0 0 1-1.455-4.405l-.837-.836zm1.588-2.653.708.707a5 5 0 0 1 7.07 7.07l.707.707a6 6 0 0 0-8.484-8.484zm-2.172-.051a.5.5 0 0 1 .708 0l12 12a.5.5 0 0 1-.708.708l-12-12a.5.5 0 0 1 0-.708z"/>
        </svg>`;
        }

        try {
          document.querySelector(`[data-brightness="${id}"]`).innerHTML = `<div
              class="d-flex flex-column justify-content-center align-items-center"
            >
              <button
                data-type="brighten"
                data-id="${id}"
                class="btn btn-outline-light cbtnl"
              >
              ${btn_bright}
              </button>
              <div class="cbtnl"><strong>${lumen}</strong></div>
              <button
                data-type="darken"
                data-id="${id}"
                class="btn btn-outline-light cbtnl"
              >
              ${btn_dark}
              </button>
            </div>`;
        } catch (TypeError) {}

        document.querySelectorAll(`[data-id="${id}"]`).forEach((button) => {
          if (button.dataset.type == "brighten") {
            button.addEventListener("click", () => brighten(id));
          } else if (button.dataset.type == "darken") {
            button.addEventListener("click", () => darken(id));
          }
        });
      });
    });
}

// Follow user
function follow(id) {
  const user_id = JSON.parse(document.getElementById("user_id").textContent);
  fetch(`/get_user/${id}`, {
    method: "PUT",
    headers: { "X-CSRFToken": csrftoken },
    mode: "same-origin",
    body: JSON.stringify({
      id: id,
      followers: user_id,
      add: true,
    }),
  }).then((response) => get_user(id));
}

// Unfollow user
function unfollow(id) {
  const user_id = JSON.parse(document.getElementById("user_id").textContent);
  fetch(`/get_user/${id}`, {
    method: "PUT",
    headers: { "X-CSRFToken": csrftoken },
    mode: "same-origin",
    body: JSON.stringify({
      id: id,
      followers: user_id,
      remove: true,
    }),
  }).then((response) => get_user(id));
}

function get_user(id) {
  fetch(`/get_user/${id}`)
    .then((response) => response.json())
    .then((user) => {
      // User fetched
      const id = user.id;
      // User session
      const user_id = JSON.parse(
        document.getElementById("user_id").textContent
      );

      // Number of followers
      const nr_followers = Object.keys(user.followers).length;
      document.querySelector("#nr_followers").innerHTML = nr_followers;
      // END Number of followers

      // BUTTONS
      if (user_id == id) {
        var button = ""; /* `<button
          data-type="edit"
          class="btn btn-outline-light cbtnl"
          >
          <strong>Edit Profile</strong>
           </button>` */
      } else if (user.followers.includes(user_id)) {
        var button = `<button
        data-type="follow"
        class="btn btn-outline-light cbtnl"
        >
        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="#e6ac00" class="bi bi-lightning-charge-fill" viewBox="0 0 16 16">
        <path d="M11.251.068a.5.5 0 0 1 .227.58L9.677 6.5H13a.5.5 0 0 1 .364.843l-8 8.5a.5.5 0 0 1-.842-.49L6.323 9.5H3a.5.5 0 0 1-.364-.843l8-8.5a.5.5 0 0 1 .615-.09z"/>
        </svg> <strong>Following</strong>
        </button>`;
      } else {
        var button = `<button
        data-type="unfollow"
        class="btn btn-outline-light cbtnl"
        >
        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" class="bi bi-lightning-charge-fill" viewBox="0 0 16 16">
        <path d="M11.251.068a.5.5 0 0 1 .227.58L9.677 6.5H13a.5.5 0 0 1 .364.843l-8 8.5a.5.5 0 0 1-.842-.49L6.323 9.5H3a.5.5 0 0 1-.364-.843l8-8.5a.5.5 0 0 1 .615-.09z"/>
        </svg> <strong>Not following</strong>
        </button>`;
      }
      document.querySelector(`[data-follow="${id}"]`).innerHTML = button;
      try {
        document
          .querySelector('[data-type="follow"]')
          .addEventListener("click", () => unfollow(id));
      } catch (TypeError) {}
      try {
        document
          .querySelector('[data-type="unfollow"]')
          .addEventListener("click", () => follow(id));
      } catch (TypeError) {}
      // END BUTTONS
    });
}

function edit_idea(id) {
  const idea_body = document.querySelector(`[data-id="idea-${id}"]`).value;

  if (idea_body) {
    fetch("/edit_idea", {
      method: "PUT",
      headers: { "X-CSRFToken": csrftoken },
      mode: "same-origin",
      body: JSON.stringify({
        id: id,
        idea: idea_body,
      }),
    }).then((response) => {
      fetch(`/idea/${id}`)
        .then((response) => response.json())
        .then((idea) => {
          var edited = idea.edited;
          var idea = idea.idea;
          document.querySelector(
            `[data-type="if-edited-${id}"]`
          ).innerHTML = `Edited: ${edited}`;
          document.querySelector(`[data-type="edited-idea-${id}"]`).innerHTML =
            idea;
        });
      document.querySelector(`#alert-${id}`).style.display = "none";
    });
  } else {
    fetch(`/idea/${id}`)
      .then((response) => response.json())
      .then((idea) => {
        var idea = idea.idea;
        document.querySelector(`[data-type="text-area-${id}"]`).value = idea;
      });
    document.querySelector(`#alert-${id}`).style.display = "block";
  }
}