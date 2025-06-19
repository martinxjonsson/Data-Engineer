import React, { useState } from "react";

function CreatePersonForm() {
    const [form, setForm] = useState({ name: "", age: "", student: false });

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setForm({ ...form, [name]: type === "checkbox" ? checked : value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch("http://localhost:5000/person", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(form),
        })
            .then((res) => res.json())
            .then((data) => alert("Person skapad!"))
            .catch((err) => console.error(err));
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Skapa ny person</h2>
            <input name="name" placeholder="Namn" onChange={handleChange} />
            <input name="age" placeholder="Ålder" type="number" onChange={handleChange} />
            <label>
                <input type="checkbox" name="student" onChange={handleChange} />
                Student
            </label>
            <button type="submit">Skapa</button>
        </form>
    );
}

export default CreatePersonForm;
