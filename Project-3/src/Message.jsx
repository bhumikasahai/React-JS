import React, { forwardRef } from 'react';
import { Card, CardContent, Typography } from '@mui/material';
import './Message.css';

const Message = forwardRef(({ message, username }, ref) => {
  const isUser = username === message.username;

  return (
    <div ref={ref} className={`message ${isUser ? 'message__user' : 'message__guest'}`}>
      <Card className={isUser ? "message__userCard" : "message__guestCard"}>
        <CardContent>
          <Typography variant="h5" component="h2">
            {isUser ? message.message : `${message.username || 'Unknown user'}: ${message.message}`}
          </Typography>
        </CardContent>
      </Card>
    </div>
  );
});

export default Message;
