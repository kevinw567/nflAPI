import React from "react";
import "./sidebar.css";
import { Results } from "./results";

export class Sidebar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isOpen: true,
            name: "",
            exactMatch: false,
            team: "",
            position: "",
            category: ""
        }

        this.collapseSidebar = this.collapseSidebar.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.setName = this.setName.bind(this);
        this.setPosition = this.setPosition.bind(this);
        this.setTeam = this.setTeam.bind(this);
        this.setCategory = this.setCategory.bind(this);
    }

    setName(event) {
        this.setState({ name: event.target.value });
    }

    setExactMatch(event) {
        if (event.target.exactMatch) {
            this.setState({ exactMatch: true });
        }
    }

    setPosition(event) {
        this.setState({ position: event.target.value });
    }

    setTeam(event) {
        this.setState({ team: event.target.value });
    }

    setCategory(event) {
        this.setState({ category: event.target.value });
    }

    collapseSidebar() {
        this.setState({
            isOpen: !this.state.isOpen
        });
    }

    handleSubmit(event) {
        event.preventDefault()
    }

    render() {
        if (!this.state.isOpen) {
            return (
                <div className = "closed-sidebar"> 
                    <button type="button" className="closed-collapse-button" onClick={() => this.collapseSidebar()}>
                        <i className = "bi bi-arrow-bar-right" width = "24" height = "24"> </i>
                    </button>
                </div>
            )
        }

        else {
            return (
                <div className="open-sidebar">
                    <button type="button" className="collapse-button" onClick={() => this.collapseSidebar()}>
                        <i className = "bi bi-arrow-bar-left" width = "24" height = "24"> </i>
                    </button>
                    <form onSubmit={this.handleSubmit}>
                        <div>
                            <div className = "sidebar-title"> Searchbar </div>
                        </div>
                        <br/>
                        <br/>
                        <br/>
                        <div>
                            <div>
                                <label className="category-lab" htmlFor="name">
                                    Name 
                                    <br/>
                                    <input type="text" name="name" value={this.state.name} style={{ width: "100%" }} onChange={this.setName}/>
                                    
                                    <div className = "category-label"> Exact Match 
                                        <input type="button" className="name-button" name = "exactMatch" onChange = {this.setExactMatch} />
                                    </div>
                                </label>
                            </div>
                            <div>
                                <label>
                                    Position
                                    <br/>
                                    <input type="text" name="position" style={{ width: "100%" }} onChange={this.setPosition} />
                                </label>
                            </div>
                            <div>
                                <label>
                                    Team
                                    <br/>
                                    <input type="text" name="team" style={{ width: "100%" }} onChange={this.setTeam}/>
                                </label>
                            </div>
                            <div>
                                <label>
                                    Category
                                    <br/>
                                </label>
                                <select name="category" style={{ width: "90%" }} onChange={this.setCategory}>
                                    <option disabled defaultValue>  </option>
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
                        <input type="submit" className="submit-button" onClick={() => new Results({
                            name: this.state.name.toString(),
                            position: this.state.position.toString(),
                            team: this.state.team.toString(),
                            category: this.state.category.toString()
                        }) }/>
                    </form>
                </div>
            )
        }
    }
}

export default Sidebar;