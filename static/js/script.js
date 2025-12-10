document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("form-adoption");
    const champs = form.querySelectorAll("input, textarea");

    function validerChamp(champ) {
        let valeur = champ.value.trim();
        let message = document.getElementById(champ.id + "Err");
        let valide = true;

        switch(champ.id) {
            case "nom":
                if (valeur.length < 3 || valeur.length > 20)
                    valide = false;
                break;
            case "espece":
            case "race":
            case "adresse":
            case "ville":
            case "description":
                if (valeur === "") valide = false;
                break;
            case "age":
                if (valeur === "" || isNaN(valeur) || Number(valeur) < 0 || Number(valeur) > 30) valide = false;
                break;
            case "courriel":
                const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!regexEmail.test(valeur)) valide = false;
                break;
            case "cp":
                const regexCP = /^[A-Z][0-9][A-Z][0-9][A-Z][0-9]$/; 
                if (!regexCP.test(valeur)) valide = false;
                break;
        }

        if (!valide) {
            champ.classList.add("input-erreur");
            message.classList.remove("hidden");
        } else {
            champ.classList.remove("input-erreur");
            message.classList.add("hidden");
        }

        return valide;
    }

    champs.forEach(champ => {
        champ.addEventListener("blur", function() {
            validerChamp(champ);
        });
    });

    form.addEventListener("submit", function(e) {
        let tousValides = true;
        champs.forEach(champ => {
            if (!validerChamp(champ)) tousValides = false;
        });

        if (!tousValides) e.preventDefault(); 
    });
});
