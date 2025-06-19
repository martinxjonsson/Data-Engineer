import React, { useEffect, useState } from "react";

function PersonList() {
    const [persons, setPersons] = useState([]);

    useEffect(() => {
        fetch("http://localhost:5000/person")
            .then((res) => res.json())
            .then((data) => setPersons(data.person_list))
            .catch((err) => console.error(err));
    }, []);

    return (
        <div>
            <h2>Personer</h2>
            <ul>
                {persons.map((p) => (
                    <li key={p.id}>
                        {p.name} – {p.age} år – {p.student ? "Student" : "Ej student"}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default PersonList;
