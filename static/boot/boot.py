from time import sleep


BOOT_SEQUENCE = [
    {
        "text": "Initializing PortfolioOS V1.32.7",
        "delay": 0.8
    },
    {
        "text": "",
        "delay": 0.3
    },
    {
        "text": "Initializing kernel...",
        "delay": 0.6
    },
    {
        "text": "Loading shell engine...",
        "delay": 0.7
    },
    {
        "text": "Mounting virtual filesystem...",
        "delay": 0.7
    },
    {
        "text": "Loading command modules...",
        "delay": 0.7
    },
    {
        "text": "Connecting services...",
        "delay": 0.8
    },
    {
        "text": "Checking environment...",
        "delay": 0.6
    },
    {
        "text": "",
        "delay": 0.3
    },
    {
        "text": "System ready.",
        "delay": 0.8
    },
    {
        "text": "",
        "delay": 0.2
    },
    {
        "text": "Welcome to Portfolio OS.",
        "delay": 0.6
    },
    {
        "text": "Type 'help' to begin.",
        "delay": 0.6
    }
]


def get_boot_sequence():

    return BOOT_SEQUENCE