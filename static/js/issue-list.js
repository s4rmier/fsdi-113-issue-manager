let todoList = document.getElementById('issue-todo');
let inProgressList = document.getElementById('issue-inprogress');
let doneList = document.getElementById('issue-done');

let toDoButton = document.getElementById('to-do-btn');
let inProgressButton = document.getElementById('in-progress-btn');
let doneButton = document.getElementById('done-btn');

function toggleListVisibility(list, button, listClass, buttonClass) {
    list.classList.remove('hidden');
    button.classList.add('active-filter');

    // Hide other lists and buttons
    [todoList, inProgressList, doneList].forEach((listItem) => {
        if (listItem !== list) {
            listItem.classList.add('hidden');
        }
    });

    // Remove active-filter class from other buttons
    [toDoButton, inProgressButton, doneButton].forEach((btn) => {
        if (btn !== button) {
            btn.classList.remove('active-filter');
        }
    });
}

toDoButton.addEventListener("click", () => {
    toggleListVisibility(todoList, toDoButton, inProgressList, doneList, inProgressButton, doneButton);
});

inProgressButton.addEventListener("click", () => {
    toggleListVisibility(inProgressList, inProgressButton, todoList, doneList, toDoButton, doneButton);
});

doneButton.addEventListener("click", () => {
    toggleListVisibility(doneList, doneButton, inProgressList, todoList, inProgressButton, toDoButton);
});
