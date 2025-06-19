import React, { useState } from "react";

function CreateAttributeForm() {
    const [form, setForm] = useState({
        attribute_name: "",
        attribute_description: "",
        attribute_value: "",
        person_id: ""
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setForm((prev) => ({ ...prev, [name]: value }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch("http://localhost:5000/attribute", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                ...form,
                person_id: parseInt(form.person_id)
            }),
        })
            .then((res) => res.json())
            .then((data) => {
                alert("Attribut skapat!");
                setForm({
                    attribute_name: "",
                    attribute_description: "",
                    attribute_value: "",
                    person_id: ""
                });
            })
            .catch((err) => console.error(err));
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Skapa nytt attribut</h2>
            <input
                name="attribute_name"
                placeholder="Namn"
                value={form.attribute_name}
                onChange={handleChange}
                required
            />
            <input
                name="attribute_description"
                placeholder="Beskrivning"
                value={form.attribute_description}
                onChange={handleChange}
            />
            <input
                name="attribute_value"
                placeholder="Värde"
                value={form.attribute_value}
                onChange={handleChange}
                required
            />
            <input
                name="person_id"
                type="number"
                placeholder="Person ID"
                value={form.person_id}
                onChange={handleChange}
                required
            />
            <button type="submit">Skapa attribut</button>
        </form>
    );
}

export default CreateAttributeForm;
