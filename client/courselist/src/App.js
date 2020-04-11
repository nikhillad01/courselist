import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import { Card, Button } from "react-bootstrap";
import axios from "axios";
import { isSuccessResponse, isNonEmptyArray } from "./helpers";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      courses: [],
    };
  }
  componentWillMount() {
    // Fetches course list and sets state value
    axios
      .get("http://127.0.0.1:8000/api/courses/")
      .then((response) => {
        if (isSuccessResponse(response)) {
          this.setState({ courses: response.data });
          return;
        }
      })
      .catch((error) => {
        if (error.hasOwnProperty("message")) {
          return error.message;
        } else {
          return "Something went wrong !";
        }
      });
  }
  render() {
    return (
      <div className="App">
        <center>
          <h3>Courses List</h3>
          <div className="cards-row">
            {isNonEmptyArray(this.state.courses) ? (
              <React.Fragment>
                {this.state.courses.map((course, i) => (
                  <Card style={{ width: "18rem" }} key={i}>
                    <Card.Img variant="top" src={course.image_src} />
                    <Card.Body>
                      <Card.Title>
                        {/* prints only first 40 characters from course name  */}
                        {course.name.slice(0, 40)}{" "}
                        {course.name.length > 40 ? <span>...</span> : null}
                      </Card.Title>
                      <Card.Text>
                        <div>
                          <strong>Author</strong> : {course.author}
                        </div>
                        <div>
                          <strong>Price</strong> : {course.price}
                        </div>
                        {course.description.slice(0, 150)}{" "}
                        {course.description.length > 150 ? (
                          <span>...</span>
                        ) : null}
                      </Card.Text>
                      <Button id="button" variant="light">
                        Enroll
                      </Button>
                    </Card.Body>
                  </Card>
                ))}
              </React.Fragment>
            ) : (
              <div>Something went wrong !</div>
            )}
          </div>
        </center>
      </div>
    );
  }
}

export default App;
