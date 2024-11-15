    <script>
        // Get the 'name' parameter from the URL
        const params = new URLSearchParams(window.location.search);
        const name = params.get("name");

        // Vulnerable code: directly inserting user input into the DOM
        if (name) {
            document.getElementById("greeting").innerHTML = "Hello, " + name + "!";
        }
    </script>
