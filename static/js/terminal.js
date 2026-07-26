document.addEventListener("DOMContentLoaded", async () => {

    await startBoot();

    document.addEventListener("click", () => {

        terminal.focus();

    });

    terminal.input.addEventListener("input", () => {

        historyManager.reset();

    });

    terminal.input.addEventListener("keydown", async (event) => {

        if (!window.bootFinished) {

            return;

        }

        switch (event.key) {

            case "ArrowUp":

                event.preventDefault();

                terminal.input.value =
                    historyManager.previous(
                        terminal.input.value
                    );

                break;

            case "ArrowDown":

                event.preventDefault();

                terminal.input.value =
                    historyManager.next();

                break;

            case "Tab":

                event.preventDefault();

                terminal.input.value =
                    autocomplete.complete(
                        terminal.input.value
                    );

                break;

            case "Enter":

                event.preventDefault();

                const command = terminal.input.value.trim();

                terminal.input.value = "";

                if (!command) return;

                historyManager.add(command);

                terminal.printCommand(command);

                const response = await api.execute(command);

                if(response.cwd){

                    terminal.updatePrompt(
                        response.cwd
                    );

                }

                for (const line of response.output) {

                    if (line === "__CLEAR__") {

                        terminal.clear();

                        continue;

                    }

                    terminal.print(line);

                }

                break;

        }

        if (event.ctrlKey && event.key === "c") {

            event.preventDefault();

            terminal.print("^C");

            terminal.input.value = "";

        }

        if (event.ctrlKey && event.key.toLowerCase() === "l") {

            event.preventDefault();

            terminal.clear();

        }

    });

});