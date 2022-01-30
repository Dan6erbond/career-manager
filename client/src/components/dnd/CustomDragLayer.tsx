import { Box } from "@chakra-ui/react";
import { Identifier } from "dnd-core/dist/types/interfaces";
import React, { CSSProperties } from "react";
import { useDragLayer, XYCoord } from "react-dnd";

const layerStyles: CSSProperties = {
  position: "fixed",
  pointerEvents: "none",
  zIndex: 100,
  left: 0,
  top: 0,
  width: "100%",
  height: "100%",
};

function getItemStyles(
  initialOffset: XYCoord | null,
  currentOffset: XYCoord | null
) {
  if (!initialOffset || !currentOffset) {
    return {
      display: "none",
    };
  }
  let { x, y } = currentOffset;
  const transform = `translate(${x}px, ${y}px)`;
  return {
    transform,
    WebkitTransform: transform,
  };
}

interface DragItemLayer<T> {
  itemType: Identifier | Identifier[];
  render: (item: T) => React.ReactNode;
}

interface CustomDragLayerProps {
  itemLayers: DragItemLayer<any>[];
}

export const CustomDragLayer = ({ itemLayers }: CustomDragLayerProps) => {
  const { itemType, isDragging, item, initialOffset, currentOffset } =
    useDragLayer((monitor) => ({
      item: monitor.getItem(),
      itemType: monitor.getItemType(),
      initialOffset: monitor.getInitialSourceClientOffset(),
      currentOffset: monitor.getSourceClientOffset(),
      isDragging: monitor.isDragging(),
    }));

  if (!isDragging) {
    return null;
  }

  function renderItem() {
    if (!itemType) {
      return;
    }
    for (const itemLayer of itemLayers) {
      if (typeof itemLayer.itemType === "string") {
        if (itemLayer.itemType === itemType) {
          return itemLayer.render(item);
        }
      } else if (Array.isArray(itemLayer.itemType)) {
        if (itemLayer.itemType.includes(itemType))
          return itemLayer.render(item);
      }
    }
  }

  return (
    <Box style={layerStyles}>
      <Box style={getItemStyles(initialOffset, currentOffset)}>
        {renderItem()}
      </Box>
    </Box>
  );
};
