import React, { useEffect, useState } from "react";

function AttributeList() {
    const [attributes, setAttributes] = useState([]);

    useEffect(() => {
        fetch("http://localhost:5000/attribute")
            .then((res) => res.json())
            .then((data) => setAttributes(data.attribute_list))
            .catch((err) => console.error(err));
    }, []);

    return (
        <div>
            <h2>Attribut</h2>
            <ul>
                {attributes.map((a) => (
                    <li key={a.id}>
                        <strong>{a.attribute_name}</strong> ({a.attribute_description}) – {a.attribute_value} (Person ID: {a.person_id})
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default AttributeList;