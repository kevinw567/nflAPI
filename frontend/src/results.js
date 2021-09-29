import React from "react";
import "./App.css";

export class Results extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
        loading: true,
        results: []
        }
    }
    

    async componentDidMount() {
        const url = "http://127.0.0.1:5000/stats/nfl/rushing?team=NWE&yds=>-1";
        const response = await fetch(url);
        const data = await response.json();
        this.setState({
            loading: false,
            results: data
        });
    }

    render() {
        return (
            this.state.loading ? (
                <React.Fragment>
                    <table className = "results-table">
                        <thead>
                            <th className = "cell"> Name </th>
                            <th className = "cell"> Position </th>
                            <th className = "cell"> Team </th> 
                        </thead>
                    </table>
                    <div className = "no-results"> No results were found </div> 
                </React.Fragment>
            ) : (
                <React.Fragment>
                    <table className = "results-table">
                        <thead>
                            <th className = "cell"> Name </th>
                            <th className = "cell"> Position </th>
                            <th className = "cell"> Team </th> 
                        </thead>
                        <tbody>
                            { this.state.results.map((player) => (
                                <tr>
                                    <td className = "cell"> { player.name } </td>
                                    <td className = "cell"> { player.position } </td>
                                    <td className = "cell"> { player.team } </td> 
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </React.Fragment>
            )
        )
    }
}