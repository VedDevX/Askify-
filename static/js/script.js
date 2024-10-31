// Toggle theme functionality with animated transitions
function toggleMode() {
    document.body.classList.toggle("dark-mode");
    const modeToggleButton = document.querySelector(".mode-toggle");
    if (document.body.classList.contains("dark-mode")) {
        modeToggleButton.textContent = "🌞 Light Mode";
    } else {
        modeToggleButton.textContent = "🌙 Dark Mode";
    }
}

// Generate questions with structured response formatting
function generateQuestions() {
    const paragraph = document.getElementById("paragraph-input").value;
    const numQuestions = document.getElementById("question-count").value;
    const resultsDiv = document.getElementById("results");
    const qaList = document.getElementById("qaList");
    const loadingSpinner = document.getElementById("loading");

    // Clear previous results
    qaList.innerHTML = "";

    // Show loading spinner with "Generating questions..." message
    loadingSpinner.classList.remove("hidden");  // Show spinner
    loadingSpinner.textContent = "Generating questions...";
    resultsDiv.classList.remove("hidden");

    fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ paragraph, num_questions: numQuestions })
    })
    .then(response => response.json())
    .then(data => {
        loadingSpinner.classList.add("hidden"); // Hide spinner after getting response
        resultsDiv.classList.remove("hidden");  // Show results

        // Add the title element if questions are generated
        if (data.questions.length > 0) {
            const titleElem = document.createElement("div");
            titleElem.id = "qaTitle";
            titleElem.textContent = "Generated Questions and Answers";
            qaList.appendChild(titleElem);

            data.questions.forEach(([question, answer]) => {
                const questionElem = document.createElement("p");
                questionElem.className = "question";
                questionElem.innerHTML = `<strong>Q:</strong> ${question}`;

                const answerElem = document.createElement("div");
                answerElem.className = "answer";
                answerElem.innerHTML = `<strong>A:</strong> ${answer}`;

                qaList.appendChild(questionElem);
                qaList.appendChild(answerElem);
            });
        } else {
            qaList.innerHTML = "<p>No questions generated. Please try again.</p>";
        }
    })
    .catch(error => {
        console.error("Error:", error);
        loadingSpinner.classList.add("hidden"); // Hide spinner on error
        resultsDiv.classList.remove("hidden");  // Show results
        qaList.innerHTML = "<p>An error occurred. Please try again later.</p>";
    });
}
