import { Box } from "@chakra-ui/react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Home } from "./pages/home";

function App() {
  return (
    <Box className="App">
      <BrowserRouter>
        <Box p={4}>
          <Routes>
            <Route path="/" element={<Home />} />
          </Routes>
        </Box>
      </BrowserRouter>
    </Box>
  );
}

export default App;
