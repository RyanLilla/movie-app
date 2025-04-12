import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import SearchMovie from "./components/SearchMovie";
import Home from "./components/Home";
import About from "./components/About";
import "./App.css";
import WatchedMovies from "./components/WatchedMovies";

function App() {
  return (
    <Router>
      <div className="app-container">
        <Navbar />
        <div className="page-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/search" element={<SearchMovie />} />
            <Route path="/watched" element={<WatchedMovies />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;