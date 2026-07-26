class AutoComplete {

    constructor() {

        this.commands = [];

    }

    setCommands(commands) {

        this.commands = commands;

    }

    complete(value) {

        const matches = this.commands.filter(cmd =>
            cmd.startsWith(value)
        );

        if (matches.length === 1) {

            return matches[0];

        }

        return value;

    }

}

const autocomplete = new AutoComplete();