import { AddIcon, ChevronDownIcon, HamburgerIcon } from "@chakra-ui/icons";
import {
  Box,
  Button,
  Flex,
  Heading,
  Menu,
  MenuButton,
  MenuItem,
  MenuList,
} from "@chakra-ui/react";
import { Link, Route, Routes } from "react-router-dom";
import { CVOverview } from "./pages/cvs";
import { CreateCV } from "./pages/cvs/create";
import { DndShowcase } from "./pages/dnd-showcase";

function App() {
  return (
    <Box className="App">
      <Flex as="nav" shadow="md" p={4} align="center">
        <Heading as={Link} to="/" size="lg">
          Career Manager
        </Heading>
        <Box flexGrow={1} />
        <Menu>
          <MenuButton as={Button} rightIcon={<ChevronDownIcon />}>
            CVs
          </MenuButton>
          <MenuList>
            <MenuItem as={Link} to="/cvs" icon={<HamburgerIcon />}>
              Overview
            </MenuItem>
            <MenuItem as={Link} to="/cvs/create" icon={<AddIcon />}>
              Create
            </MenuItem>
          </MenuList>
        </Menu>
      </Flex>
      <Box p={4}>
        <Routes>
          <Route path="/cvs" element={<CVOverview />} />
          <Route path="/cvs/create" element={<CreateCV />} />
          <Route path="/dnd-showcase" element={<DndShowcase />} />
        </Routes>
      </Box>
    </Box>
  );
}

export default App;
