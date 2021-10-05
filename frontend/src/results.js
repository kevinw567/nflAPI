import React from "react";
import "./App.css";

export class Results extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            loading: false,
            search_criteria: {
                name: this.props.name,
                position: this.props.position,
                team: this.props.team,
                category: this.props.category
            },
            results: [{
                    name: "Tom Brady",
                    position: "QB",
                    team: "TB"
                },
                {
                    name: "Patrick Mahomes",
                    position: "QB",
                    team: "KC"
                },
                {
                    name: "Mac Jones",
                    position: "QB",
                    team: "NE"
            }]
        }
    }

    async componentDidMount() {
        try {
            let baseurl = "http://127.0.0.1:5000/stats/nfl/"
            baseurl += this.state.search_criteria["category"] + "?"
            for (let prop in this.state.search_criteria) {
                if (prop && prop !== "" && prop !== "category") {
                    baseurl += prop + "=" + this.state.search_criteria[prop] + "&";
                }
            }
            baseurl.substring(0, baseurl.length - 1);
            const url = "http://127.0.0.1:5000/stats/nfl/rushing?team=NWE&yds=>-1";
            console.log(baseurl);
            const response = await fetch(url);
            const data = await response.json();
            this.setState({
                loading: false,
                results: data
            });
        }

        catch (err) {
            return
        }
    }

    render() {
        return (
            this.state.search_criteria.name !== "" ? (
                <React.Fragment>
                    <table className = "results-table">
                        <thead>
                            <tr>
                                <th className = "cell"> Name </th>
                                <th className = "cell"> Position </th>
                                <th className = "cell"> Team </th>
                            </tr>
                        </thead>
                        <div className = "no-results"> No results were found </div>
                    </table>
                </React.Fragment>
            ) : (
                <React.Fragment>
                    <table className = "results-table">
                            <thead>
                                <tr>
                                    <th className = "cell"> Name </th>
                                    <th className = "cell"> Position </th>
                                    <th className = "cell"> Team </th>
                                </tr> 
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

export default Results;