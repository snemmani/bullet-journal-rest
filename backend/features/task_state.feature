Feature: Manage Task State

    Scenario: Create a new task existing task state
        Given a task state is already created
          When the user selects an existing task State
          Then a task is successfully created

    Scenario: Create a new task with a new task state
        Given a task state is already created
          When the user selects a new task State
          Then throw an error that a new task cannot be created

    Scenario: Creating a new task without a description
    Given a user creates a new task with a due date
        When a user creates a task
        Then reject the entry and send user the error

    Scenario: Creating a new task with a description and without a due date
    Given a user creates a new task without a new date
        When a user creates a task
        Then create the task and send the info back to user