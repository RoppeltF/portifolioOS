class HistoryManager {

    constructor(max = 10) {

        this.max = max;

        this.history = [];

        this.index = 0;

        this.savedInput = "";

    }


    add(command) {

        if (!command.trim()) {
            return;
        }

        if (this.history[this.history.length - 1] !== command) {

            this.history.push(command);

        }

        if (this.history.length > this.max) {

            this.history.shift();

        }

        this.index = this.history.length;

    }


    previous(currentInput) {

        if (!this.history.length) {

            return currentInput;

        }

        if (this.index === this.history.length) {

            this.savedInput = currentInput;

        }

        if (this.index > 0) {

            this.index--;

        }

        return this.history[this.index];

    }


    next() {

        if (!this.history.length) {

            return "";

        }

        if (this.index < this.history.length - 1) {

            this.index++;

            return this.history[this.index];

        }

        this.index = this.history.length;

        return this.savedInput;

    }


    reset() {

        this.index = this.history.length;

    }

}

const historyManager = new HistoryManager();