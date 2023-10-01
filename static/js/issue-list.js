let todoList = document.getElementById('issue-todo');
let inProgressList = document.getElementById('issue-inprogress');
let doneList = document.getElementById('issue-done');

let toDoButton = document.getElementById('to-do-btn');
let inProgressButton = document.getElementById('in-progress-btn');
let doneButton = document.getElementById('done-btn');

let toggleVisibility = (list, button) => {

    function toggleListsState(listClass) {
        listClass.classList.remove('hidden')
        let listArray = [todoList, inProgressList, doneList]

        listArray.forEach(list => {
            if (list != listClass) {
                list.classList.add('hidden')
            }
        });
    }

    function toggleFilterState(buttonClass) {
        buttonClass.classList.add('active-filter')
        let buttonsArray = [toDoButton, inProgressButton, doneButton]

        buttonsArray.forEach(button => {
            if (button != buttonClass) {
                button.classList.remove('active-filter')
            }
        });
    }

    toggleListsState(list);
    toggleFilterState(button);
}

toDoButton.addEventListener("click", () => {
    toggleVisibility(todoList, toDoButton)
})

inProgressButton.addEventListener("click", () => {
    toggleVisibility(inProgressList, inProgressButton)
})

doneButton.addEventListener("click", () => {
    toggleVisibility(doneList, doneButton)
})