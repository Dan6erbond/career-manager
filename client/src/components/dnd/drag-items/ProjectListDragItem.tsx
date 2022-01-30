import { DragHandleIcon } from "@chakra-ui/icons";
import { Box, HStack, Text } from "@chakra-ui/react";
import React from "react";
import { Project } from "../../../types/Project";
import { DragItemProps } from "./generics";

export const ProjectListDragItem = ({ item }: DragItemProps<Project>) => (
  <Box rounded="md" shadow="md" p={4} bg="gray.50">
    <HStack spacing={2}>
      <DragHandleIcon />
      <Text>{item.description}</Text>
    </HStack>
  </Box>
);
