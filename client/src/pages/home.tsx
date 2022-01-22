import { Heading, VStack } from "@chakra-ui/react";
import { useCallback, useState } from "react";
import {
  ProjectListItem,
  ProjectListItemDragLayer,
} from "../components/projects/ProjectListItem";
import { projects as projectList } from "../lib/projects";

export const Home = () => {
  const [projects, setProjects] = useState(projectList);

  const moveIndex = useCallback(
    (id: number, to: number) => {
      setProjects((projects) => {
        const project = projects.find((project) => project.id === id);
        const newProjects = [...projects];
        if (project !== undefined) {
          newProjects.splice(
            to,
            0,
            newProjects.splice(projects.indexOf(project), 1)[0]
          );
        }
        return newProjects;
      });
    },
    [setProjects]
  );

  return (
    <VStack spacing={4} align="stretch">
      <Heading>Projects</Heading>
      <VStack spacing={2} align="stretch">
        <ProjectListItemDragLayer />
        {projects.map((project, index) => (
          <ProjectListItem
            key={project.id}
            project={project}
            moveIndex={moveIndex}
            index={index}
          />
        ))}
      </VStack>
    </VStack>
  );
};
