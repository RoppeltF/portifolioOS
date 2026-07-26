window.bootFinished = false;

window.skipBoot = false;

async function startBoot() {

    const boot = await api.boot();

    for (const item of boot) {

        if (window.skipBoot) {

            break;

        }

        await terminal.type(item.text);

        if (!window.skipBoot) {

            await new Promise(r =>
                setTimeout(r, item.delay * 1000)
            );

        }

    }

    terminal.showPrompt();

    window.bootFinished = true;

}

document.addEventListener("keydown", () => {

    if (!window.bootFinished) {

        window.skipBoot = true;

    }

});