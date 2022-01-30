import { ChevronDownIcon } from "@chakra-ui/icons";
import {
  Button,
  Code,
  Container,
  FormControl,
  FormHelperText,
  FormLabel,
  Heading,
  HStack,
  Input,
  Menu,
  MenuButton,
  MenuItem,
  MenuList,
  Text,
  VStack,
} from "@chakra-ui/react";
import React from "react";
import { DndShowcase } from "../dnd-showcase";

export const CreateCV = () => {
  return (
    <Container maxW="container.lg" p={4}>
      <HStack spacing={[4, 6, 8]} alignSelf="stretch" align="start">
        <VStack spacing={4} flex={1} align="stretch">
          <Heading>Create a new CV</Heading>
          <VStack as="form" spacing={4} align="stretch">
            <FormControl>
              <FormLabel>Title</FormLabel>
              <Input placeholder="Title" />
              <FormHelperText>
                Title can be interpolated with variables such as{" "}
                <Code>{"{firstname}"}</Code>, <Code>{"{lastname}"}</Code>,{" "}
                <Code>{"{lang}"}</Code> and <Code>{"{date}"}</Code>.
              </FormHelperText>
            </FormControl>
            <FormControl>
              <FormLabel>Headline</FormLabel>
              <HStack align="end" spacing={2}>
                <Menu>
                  <MenuButton
                    flexShrink={0}
                    as={Button}
                    rightIcon={<ChevronDownIcon />}
                  >
                    English
                  </MenuButton>
                  <MenuList>
                    <MenuItem>Overview</MenuItem>
                    <MenuItem>Create</MenuItem>
                  </MenuList>
                </Menu>
                <Input placeholder="Headline" />
              </HStack>
            </FormControl>
            <Text fontWeight="medium">Skills & Projects</Text>
          </VStack>
        </VStack>
        <DndShowcase />
      </HStack>
    </Container>
  );
};
