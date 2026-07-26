class TerminalUI {

    constructor() {

   this.output = document.getElementById("output");

    this.prompt = document.getElementById("prompt");

    this.input = document.getElementById("command");


    // terminal components
    this.user = document.getElementById("user");
    this.path = document.getElementById("path");
    this.symbol = document.getElementById("symbol");

    }


    showPrompt() {

        this.prompt.style.display = "flex";

        this.input.focus();

    }


    focus() {

        this.input.focus();

    }


    clear() {

        this.output.innerHTML = "";

    }


    printCommand(command) {

    const div =
        document.createElement("div");


    div.className = "line";


    div.innerHTML = `

        <span class="green">
        ${this.user.textContent}
        </span>

        :

        <span class="blue">
        ${this.path.textContent}
        </span>

        ${this.symbol.textContent}

        ${command}

    `;


    this.output.appendChild(div);


    this.scroll();

    }


    print(text = "") {

        const lines = text.split("\n");

        for (const line of lines) {

            const div = document.createElement("div");

            div.className = "line";

            div.textContent = line;

            this.output.appendChild(div);

        }

        this.scroll();

    }


    async type(text) {

        const div = document.createElement("div");

        div.className = "line";

        this.output.appendChild(div);

        for (const c of text) {

            if (window.skipBoot) {

                div.textContent = text;

                break;

            }

            div.textContent += c;

            await new Promise(r => setTimeout(r, 20));

        }

        this.scroll();

    }

    updatePrompt(cwd) {

    let displayPath = cwd;


    displayPath = displayPath.replace(
        "/home/roberto",
        "~"
    );


    this.user.textContent =
        "roberto@portfolioOS";


    this.path.textContent =
        displayPath;


    this.symbol.textContent =
        "$";

    }

    scroll() {

        window.scrollTo(0, document.body.scrollHeight);

    }

}

const terminal = new TerminalUI();