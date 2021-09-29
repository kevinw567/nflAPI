import React from "react";
import "./sidebar.css";

export class Sidebar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isOpen: true,
            search_criteria: []
        }

        this.collapseSidebar = this.collapseSidebar.bind(this);
    }

    collapseSidebar() {
        this.setState({
            isOpen: !this.state.isOpen
        });
    }

    render() {
        if (!this.state.isOpen) {
            return (
                <div className = "closed-sidebar"> 
                    <button type = "button" className = "closed-collapse-button" onClick = { () => this.collapseSidebar() }> ||| </button>
                </div>
            )
        }

        else {
            return (
                <div className = "open-sidebar">
                    <button type = "button" className = "collapse-button" onClick = { () => this.collapseSidebar() }> ||| </button>
                    <form>
                        <div className = "sidebar-title">
                            Searchbar
                        </div>
                        <div>
                            <div>
                                <label className = "category-lab" for = "name"> Name </label>
                                <br/>
                                <input type = "text" name = "name" style = {{ width: "100%" }}/>
                                <br/>
                                Exact Match <input type = "button" className = "name-button"/>
                            </div>
                            <div>
                                Position
                                <br/>
                                <input type = "text" name = "position" style = {{ width: "100%" }}/>
                            </div>
                            <div>
                                Team
                                <br/>
                                <input type = "text" name = "name" style = {{ width: "100%" }}/>
                            </div>
                            <div style = {{ width: "100%" }}>
                                Category
                                <br/>
                                <select name = "category" style = {{ width: "90%" }}>
                                    <option disabled selected>  </option>
                                    <option value = "passing"> Passing </option>
                                    <option value = "rushing"> Rushing</option>
                                    <option value = "receiving"> Receiving</option>
                                    <option value = "defense"> Defense </option>
                                    <option value = "returns"> Returns </option>
                                    <option value = "scrimmage"> Scrimmage </option>
                                    <option value = "scoring"> Scoring </option>
                                </select>    
                            </div>
                        </div>
                        <input type = "submit" className = "submit-button"/>
                    </form>
                </div>
            )
        }
    }
}