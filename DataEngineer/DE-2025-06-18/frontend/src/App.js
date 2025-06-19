import React from "react";
import PersonList from "./PersonList";
import AttributeList from "./AttributeList";
import CreatePersonForm from "./CreatePersonForm";
import CreateAttributeForm from "./CreateAttributeForm";


function App() {
  return (
    <div className="App">
      <h1>Database by MaRtIn JoNsSoN</h1>
      <CreatePersonForm />
      <CreateAttributeForm />
      <PersonList />
      <AttributeList />
    </div>
  );
}

export default App;
