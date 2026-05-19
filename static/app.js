const chatBox = document.getElementById("chat-box");
const input = document.getElementById("message-input");

function addMessage(text, sender) {

    const div = document.createElement("div");

    div.classList.add("message");
    div.classList.add(sender);

    div.innerText = text;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {

    const message = input.value.trim();

    if (!message) return;

    addMessage(message, "user");

    input.value = "";

    try {

        const response = await fetch(
    "http://127.0.0.1:8000/chat",
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            session_id: "user1",
            message: message
        })
    }
);

        const data = await response.json();

        addMessage(data.reply, "bot");

    } catch (error) {

        addMessage(
            "Error connecting to server",
            "bot"
        );
    }
}

input.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }
});