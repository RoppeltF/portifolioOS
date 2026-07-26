class TerminalAPI {

    async execute(command) {

        const response = await fetch("/api/command", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                command: command
            })

        });

        return await response.json();

    }


    async boot() {

        const response = await fetch("/api/boot");

        return await response.json();

    }

}

const api = new TerminalAPI();