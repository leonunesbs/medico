FROM node:lts

RUN mkdir /app/
WORKDIR /app/
ADD package.json /app/package.json
RUN yarn install
ADD . /app/

CMD ["yarn", "start"]
