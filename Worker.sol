
pragma solidity >=0.6.0 <0.8.0;

contract Worker {
    struct Task {
        bool assigned;
        uint completionTime;
    }

    mapping(string => Task) tasks;
    uint taskId = 0;

    event TaskAssigned(string indexed name, uint indexed id);
    event TaskCompleted(string indexed name, uint indexed id, uint completionTime);

    function assignTask(string memory name) public {
        require(!tasks[name].assigned, "Task already assigned");
        Task storage task = tasks[name];
        task.assigned = true;
        task.completionTime = block.timestamp + 1 minutes;

        emit TaskAssigned(name, ++taskId);
    }

    function completeTask(string memory name) public {
        require(tasks[name].assigned, "Task not assigned");
        require(tasks[name].completionTime < block.timestamp, "Task not due");

        delete tasks[name];

        emit TaskCompleted(name, taskId, block.timestamp);
    }
