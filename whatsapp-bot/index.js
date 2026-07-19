require("dotenv").config();

const { Client, LocalAuth } = require("whatsapp-web.js");
const qrcode = require("qrcode-terminal");
const axios = require("axios");

const client = new Client({
    authStrategy: new LocalAuth({
        clientId: "AttendAI"
    }),

    puppeteer: {
        headless: true,

        executablePath: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",

        args: [
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-dev-shm-usage"
        ]
    }
});


client.on("qr", (qr) => {

    console.log("\nScan this QR using WhatsApp\n");

    qrcode.generate(qr, {
        small: true
    });

});


client.on("ready", () => {

    console.log("\n================================");
    console.log("AttendAI WhatsApp Bot Connected");
    console.log("================================\n");

});


client.on("authenticated", () => {

    console.log("WhatsApp Authenticated");

});


client.on("auth_failure", msg => {

    console.log("Authentication Failed");
    console.log(msg);

});


client.on("disconnected", reason => {

    console.log("Disconnected");
    console.log(reason);

});


client.on("message", async message => {

    console.log("Message:", message.body);

    try {

        const response = await axios.post(
            process.env.FASTAPI_URL + "/ai/chat",
            {
                message: message.body
            }
        );

        await message.reply(
            JSON.stringify(response.data, null, 2)
        );

    }

    catch (error) {

        console.log(error.message);

        await message.reply(
            "❌ AttendAI Server Offline"
        );

    }

});


client.initialize();